import streamlit as st
from evaluator import build_graph

st.set_page_config(page_title="AI Essay Evaluator — Groq + LangGraph", layout="wide")
st.title("🧠 Project 4 — AI Essay Evaluator (Groq + LangGraph)")
st.markdown("Evaluate your essay across **language**, **analysis**, and **clarity** using Groq LLM intelligence.")

essay_text = st.text_area("✍️ Paste your essay below:", height=350)

if st.button("Evaluate Essay"):
    if not essay_text.strip():
        st.warning("Please paste an essay before running the evaluation.")
    else:
        with st.spinner("Evaluating your essay... ⏳"):
            graph = build_graph()
            workflow = graph
            state = {"essay": essay_text}
            result = workflow.invoke(state)

        st.subheader("📊 Evaluation Results")
        st.markdown(f"**Average Score:** {result['avg_score']:.2f}/10")
        st.divider()

        st.subheader("🔍 Detailed Feedback")
        st.markdown(f"**Language Feedback:** {result['language_feedback']}")
        st.markdown(f"**Depth of Analysis Feedback:** {result['analysis_feedback']}")
        st.markdown(f"**Clarity of Thought Feedback:** {result['clarity_feedback']}")
        st.divider()
        st.markdown(f"**🧩 Overall Feedback:** {result['overall_feedback']}")
