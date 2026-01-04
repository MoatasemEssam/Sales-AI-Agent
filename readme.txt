An end-to-end MLOps pipeline that automates corporate sales research and personalized outreach. This agent researches a company's recent business news in real-time and generates a high-conversion sales pitch.



## System Architecture
This project implements a **Decoupled Agentic Architecture**:
- **AI Brain:** Built with `LangGraph` for stateful, multi-step reasoning.
- **Service Layer:** `FastAPI` backend for high-performance model serving.
- **User Interface:** `Streamlit` dashboard for real-time human-in-the-loop interaction.
- **Monitoring:** Integrated with `LangSmith` for observability and token cost tracking.

---

##  Tech Stack
| Layer | Technology |
| :--- | :--- |
| **Orchestration** | LangGraph (Agentic Design) |
| **LLM** | OpenAI GPT-4o |
| **Search Engine** | Tavily AI (Search API for LLMs) |
| **Backend API** | FastAPI |
| **Frontend** | Streamlit |
| **MLOps Tools** | LangSmith (Tracing), python-dotenv (Security) |

---

##  Getting Started

### 1. Prerequisites
- Python 3.10+
- OpenAI API Key
- Tavily API Key

### 2. Installation
```bash
# Clone the repository
git clone [https://github.com/YOUR_USERNAME/SAB-AI-Sales-Agent.git](https://github.com/YOUR_USERNAME/SAB-AI-Sales-Agent.git)
cd SAB-AI-Sales-Agent

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
