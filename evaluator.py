from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated
from pydantic import BaseModel, Field
import operator
import os

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found. Please set it in your .env file.")

# Initialize Groq model
model = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.1-8b-instant",
    temperature=0.7,
    max_tokens=512
)

# Structured schema for LLM output
class EvaluationSchema(BaseModel):
    feedback: str = Field(description="Detailed feedback for the essay")
    score: int = Field(description="Score out of 10", ge=1, le=10)  # min 1, max 10

structured_model = model.with_structured_output(EvaluationSchema)

# Graph state
class UPSCState(TypedDict):
    essay: str
    language_feedback: str
    analysis_feedback: str
    clarity_feedback: str
    overall_feedback: str
    individual_scores: Annotated[list[int], operator.add]
    avg_score: float

# --- Evaluation Nodes ---
def evaluate_language(state: UPSCState):
    prompt = f"""
Evaluate the language quality of the following essay.

Return a JSON object with exact keys:
{{
  "feedback": "detailed feedback",
  "score": 1-10
}}

Essay:
{state['essay']}
"""
    output = output = structured_model.invoke(prompt)
    return {"language_feedback": output.feedback, "individual_scores": [output.score]}


def evaluate_analysis(state: UPSCState):
    prompt = f"""
Evaluate the depth of analysis of the following essay.

Return a JSON object with exact keys:
{{
  "feedback": "detailed feedback",
  "score": 1-10
}}

Essay:
{state['essay']}
"""
    output = output = structured_model.invoke(prompt)
    return {"analysis_feedback": output.feedback, "individual_scores": [output.score]}


def evaluate_thought(state: UPSCState):
    prompt = f"""
Evaluate the clarity of thought of the following essay.

Return a JSON object with exact keys:
{{
  "feedback": "detailed feedback",
  "score": 1-10
}}

Essay:
{state['essay']}
"""
    output = output = structured_model.invoke(prompt)
    return {"clarity_feedback": output.feedback, "individual_scores": [output.score]}


def final_evaluation(state: UPSCState):
    # Summarize feedbacks into overall feedback
    prompt = f"""
Based on the following feedbacks, create a summarized evaluation:

Language Feedback: {state['language_feedback']}
Depth of Analysis Feedback: {state['analysis_feedback']}
Clarity of Thought Feedback: {state['clarity_feedback']}

Return a JSON object:
{{
  "feedback": "summarized feedback",
  "score": 1-10
}}
"""
    output = output = structured_model.invoke(prompt)

    # Average score calculation
    avg_score = round(sum(state["individual_scores"]) / len(state["individual_scores"]), 1)
    avg_score = max(1, min(avg_score, 10))  # clamp just in case

    return {"overall_feedback": output.feedback, "avg_score": avg_score}


# --- LangGraph Construction ---
def build_graph():
    graph = StateGraph(UPSCState)

    graph.add_node("evaluate_language", evaluate_language)
    graph.add_node("evaluate_analysis", evaluate_analysis)
    graph.add_node("evaluate_thought", evaluate_thought)
    graph.add_node("final_evaluation", final_evaluation)

    # Edges
    graph.add_edge(START, "evaluate_language")
    graph.add_edge(START, "evaluate_analysis")
    graph.add_edge(START, "evaluate_thought")
    graph.add_edge("evaluate_language", "final_evaluation")
    graph.add_edge("evaluate_analysis", "final_evaluation")
    graph.add_edge("evaluate_thought", "final_evaluation")
    graph.add_edge("final_evaluation", END)

    return graph.compile()
