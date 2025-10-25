# 🧠 Project 5 — AI Resume Screener (NLP)

**Powered by Groq LLaMA + LangGraph + Streamlit**

---

## 📘 Overview

This project is part of the **“40 Days of AI Projects”** series.
**AI Resume Screener** leverages **Groq LLaMA 3.1-8B** for fast, structured NLP evaluation and **LangGraph** to orchestrate a multi-step reasoning workflow.

It reads a resume (or essay-like input), analyzes multiple aspects such as:

* Language quality
* Depth of analysis
* Clarity of thought

Then, it produces structured feedback with scores and a summarized evaluation.

---

## 🧩 Tech Stack

* **Groq LLaMA 3.1-8B Instant** — lightning-fast LLM inference
* **LangGraph** — visual and composable workflow orchestration
* **LangChain Groq** — interface for Groq-powered language models
* **Streamlit** — simple and interactive front-end for the user

---

## 🗂️ Folder Structure

```
AI-Resume-Screener/
│
├── app.py              # Streamlit app entry point
├── screener.py         # Core LangGraph + Groq logic
├── requirements.txt    # All dependencies
├── .env                # Contains Groq API Key
└── README.md           # Documentation
```

---

## ⚙️ Installation

1. **Clone this repo**

   ```bash
   git clone 
   cd AI-Resume-Screener
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up `.env` file**

   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

---

## 🚀 Run the Application

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🧠 How It Works

1. User inputs a **resume text** (or essay-like document).
2. The app sends the text to **LangGraph**, which coordinates three evaluators:

   * **Language Evaluator**
   * **Analysis Evaluator**
   * **Clarity Evaluator**
3. Each evaluator uses the **Groq LLaMA** model to give feedback and scores.
4. The system aggregates results into a **final feedback report** with an average score.

---

## 📊 Example Output

```
Language Feedback: Excellent grammar and clarity.
Analysis Feedback: Strong analytical insight with relevant examples.
Clarity Feedback: Clear and concise expression of ideas.
Average Score: 8.7/10
Overall Feedback: The resume reflects strong analytical thinking and structured writing.
```

---

## 🧠 Learning Outcome

* Using **Groq hardware acceleration** for ultra-fast LLM inference
* Building structured **NLP pipelines** using LangGraph
* Designing an **LLM evaluation system** with scoring
* Deploying AI workflows in **Streamlit**

---

## 💡 Next Steps

* Add job role–specific scoring (e.g., Data Scientist, ML Engineer).
* Integrate resume parsing (PDF/DOCX).
* Visualize performance trends using charts.

---

**Author:** Ujjwal
**Series:** 40 Days of AI Projects — *Day 5: AI Resume Screener (NLP)*
**License:** MIT
