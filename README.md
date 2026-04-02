# 🧠 Research Paper Explainer AI

An intelligent **Retrieval-Augmented Generation (RAG)** system that enables users to upload research papers and interactively understand them through structured explanations, diagrams, and contextual Q&A.

---

## 🚀 Overview

Understanding research papers can be time-consuming and complex, especially with dense technical content and mathematical formulations. This project aims to simplify that process by leveraging **Large Language Models (LLMs)** and **semantic retrieval**.

Users can:

* Upload a research paper (PDF)
* Get structured explanations (problem, method, insights)
* Ask questions interactively
* Generate architecture diagrams
* Understand technical concepts with examples

---

## 🧠 System Architecture

```
PDF → Text Extraction → Chunking → Embeddings → FAISS Vector Store
                                                    ↓
                                           Retriever (Top-K)
                                                    ↓
                           LLM (Explanation / Q&A / Diagram Generation)
                                                    ↓
                                     Conversational Memory
```

---

## ⚙️ Tech Stack

* **LLM Framework:** LangChain
* **Model:** OpenAI (GPT-5.4)
* **Vector Store:** FAISS (in-memory)
* **Embeddings:** OpenAI Embeddings
* **PDF Processing:** PyMuPDF
* **Frontend:** Streamlit
* **Environment Management:** python-dotenv

---

## ✨ Features

### 📘 1. Structured Paper Explanation

* Problem statement
* Methodology
* Key innovations
* Real-world applications

---

### 💬 2. Conversational Q&A

* Ask context-aware questions
* Supports follow-up queries using memory

---

### 📊 3. Diagram Generation

* Automatically generates **Mermaid diagrams**
* Helps visualize model architectures and pipelines

---

### 🔍 4. Semantic Retrieval (RAG)

* Uses embeddings + FAISS
* Retrieves relevant chunks for accurate answers
* Reduces hallucinations

---

### 🧠 5. Modular Design

* Clean separation of:

  * Core logic
  * Chains
  * Prompts
  * UI
* Easily extensible for research-level upgrades

---

## 📂 Project Structure

```
research_explainer/
│
├── app.py
├── config.py
├── requirements.txt
│
├── core/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vectorstore.py
│
├── chains/
│   ├── qa_chain.py
│   ├── explain_chain.py
│   ├── diagram_chain.py
│
├── utils/
│   └── prompts.py
```

---

## 🛠️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/research-paper-explainer-ai.git
cd research-paper-explainer-ai
```

---

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

### 5. Run the app

```
streamlit run app.py
```

---

## 🧪 Example Use Cases

* 📄 Understanding complex ML/AI research papers
* 📊 Visualizing model architectures
* 🎓 Learning new concepts interactively
* 🔬 Assisting literature review

---

## ⚠️ Limitations

* Mathematical expressions may not always be perfectly parsed
* Complex equations may require enhanced LaTeX extraction
* Figures and tables are not yet fully supported

---

## 🚀 Future Improvements

* 🔥 Multimodal understanding (figures + charts)
* 🧠 Equation-aware reasoning system
* 🤖 Agent-based architecture (LangGraph)
* 📑 Section-aware retrieval (Abstract, Method, Results)
* 🔍 Hybrid search (BM25 + embeddings)

---

## 📌 Key Concepts

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Conversational AI
* Prompt Engineering

---

## 🙌 Acknowledgements

* LangChain
* OpenAI
* FAISS
* Streamlit

---

## 💡 Author

**Souptik Dey**

---
