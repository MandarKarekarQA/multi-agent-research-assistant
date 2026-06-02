# 🤖 Multi-Agent Research Assistant
## Live Demo

- Streamlit App: YOUR_STREAMLIT_APP_URL
- GitHub Repository: YOUR_GITHUB_REPO_URL

A cost-controlled AI-powered research assistant built using local LLMs, Ollama, Mistral, LangChain, and Streamlit.

This project demonstrates a real-world multi-agent AI workflow where multiple AI agents collaborate to perform web research, summarize information, validate outputs, and generate structured reports.

---

# 🚀 Features

* 🔎 Web research agent
* 🧠 AI summarization agent
* 🕵️ Validation and quality-checking agent
* 📝 Automated report generation
* 💰 Cost tracking system
* 📂 Raw and processed data storage
* 🖥️ Streamlit UI dashboard
* 🧠 Local LLM support using Ollama + Mistral
* 📊 Pipeline metrics and execution tracking
* 📥 Downloadable Markdown reports

---

# 🏗️ Architecture

```text
User Input
   ↓
Research Agent
   ↓
Summarizer Agent
   ↓
Validator Agent
   ↓
Report Writer Agent
   ↓
Final Research Report
```

---

# 🧰 Tech Stack

## AI / LLM

* Ollama
* Mistral
* LangChain

## Frontend

* Streamlit

## Backend

* Python

## Utilities

* JSON
* Markdown
* Local File Storage

---

# 📂 Project Structure

```text
multi-agent-research-assistant/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── reports/
│
├── src/
│   ├── agents/
│   │   ├── research_agent.py
│   │   ├── summarizer_agent.py
│   │   ├── validator_agent.py
│   │   └── report_writer_agent.py
│   │
│   ├── tools/
│   │   └── search_tool.py
│   │
│   ├── utils/
│   │   ├── cost_tracker.py
│   │   └── format_sources.py
│   │
│   └── main_pipeline.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <your-github-url>
cd multi-agent-research-assistant
```

---

## 2. Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🧠 Install Ollama

Download and install Ollama:

👉 https://ollama.com/

Then pull the Mistral model:

```bash
ollama pull mistral
```

---

# ▶️ Run the Application

## Start Streamlit App

```bash
streamlit run app/streamlit_app.py
```

---

# 🖥️ Example Workflow

1. User enters research topic
2. Research agent collects web data
3. Summarizer agent creates concise insights
4. Validator agent checks quality
5. Report writer generates final report
6. User downloads final Markdown report

---

# 📊 Example Metrics

* Model Used: Mistral
* Execution Mode: Local Ollama
* Agent Count: 4
* API Cost: £0
* Execution Time: Variable depending on local hardware

---

# 💡 Why This Project?

This project demonstrates:

* Multi-agent AI architecture
* Applied AI engineering
* Local LLM integration
* AI workflow orchestration
* Cost-efficient AI systems
* Streamlit UI development
* Real-world AI product design

---

# 🔮 Future Improvements

* LangGraph integration
* Vector database memory (ChromaDB)
* RAG pipeline support
* PDF export
* Multi-model routing
* Live streaming responses
* Advanced source filtering
* Cloud deployment

---

# 👨‍💻 Author

Mandar Karekar

AI/ML Engineer | QA Automation Engineer | Applied AI Enthusiast

---

# 📜 License

This project is for educational and portfolio purposes.
