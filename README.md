# 🤖 Phidata Agents — Single & Multi-Agent AI

<p align="center">
  <b>Building AI Agents & Multi-Agent Systems with Python, Phidata, LLMs & Tools</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Phidata-AI%20Agents-orange?style=for-the-badge" alt="Phidata">
  <img src="https://img.shields.io/badge/Groq-LLM-purple?style=for-the-badge" alt="Groq">
  <img src="https://img.shields.io/badge/Gemini-Generative%20AI-blue?style=for-the-badge" alt="Gemini">
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/GitHub-Version%20Control-black?style=for-the-badge&logo=github" alt="GitHub">
</p>

---

## 📌 About the Project

This project demonstrates the fundamentals of **Agentic AI and Generative AI** using the **Phidata (Phi) framework**.

The project explores how AI agents can use **Large Language Models (LLMs), tools, web search, APIs, and specialized agents** to perform real-world tasks.

The repository includes practical implementations for:

* 💰 Financial Analysis
* 📰 Financial News
* 🏏 Cricket Information
* ₿ Cryptocurrency
* 🛒 E-Commerce Search
* ✈️ Travel Search
* 🏀 Sports News

---

## 🚀 Project Features

* 🤖 AI Agent development using **Phidata**
* 🧠 Multiple LLM integrations
* 🔎 Web search using DuckDuckGo
* 📊 Stock analysis using Yahoo Finance
* 🏏 Cricket information and news
* ₿ Cryptocurrency price lookup
* 🛒 Product search and comparison
* ✈️ Flight and hotel search
* 👥 Multi-agent workflows
* 🌐 Streamlit applications
* 🔐 Secure API key management using `.env`

---

## 📂 Project Structure

```text
phidata-ai-agents/
│
├── 📄 agents_with_python_function.py
├── 🏏 cricket_agent_gemini.py
├── 🏏 cricket_app_agent.py
├── 🤖 groq_agents.py
├── 📊 groq_agents1.py
├── 📈 multiagent_financialnew_analysis.py
├── 🤖 multiagents.py
├── 📰 news_Agents.py
├── 🦙 ollama_agents.py
├── 📓 phi_with_gemini_ai.ipynb
├── 🔐 .gitignore
└── 📄 README.md
```

---

## 💰 Financial Agents

The financial agents demonstrate how Phidata can connect an LLM with financial tools.

### Features

* 📈 Stock prices
* 📊 Stock fundamentals
* 👨‍💼 Analyst recommendations
* 📰 Financial news
* 📉 Market analysis
* 😊 Sentiment analysis

The project uses **Yahoo Finance tools** for stock information.

Example companies include:

```text
Apple
Google
Amazon
Microsoft
Tesla
Infosys
```

---

## 🏏 Cricket AI Agents

The Cricket AI project uses **Phidata + Gemini + DuckDuckGo + Streamlit**.

The agent can provide:

* 🏏 Match information
* 📊 Player statistics
* 📰 Cricket news
* 🔎 Web-based cricket information

Example:

```text
Match: India vs Australia
Player: Virat Kohli
```

The Streamlit application provides an interactive interface for entering match and player information.

---

## 👥 Multi-Agent System

The project also demonstrates multiple specialized AI agents.

```text
                    User Query
                        │
                        ▼
                ┌──────────────┐
                │  AI Agents   │
                └──────┬───────┘
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
    News Agent     Finance Agent   Search Agent
        │              │              │
        ▼              ▼              ▼
    Web Search     APIs / Tools    Web Search
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                 Final Response
```

---

## 📰 News Agent

The News Agent uses **Groq + DuckDuckGo** to:

* 🔎 Search financial news
* 📰 Find recent articles
* 📝 Summarize important information
* 📊 Present results using Markdown

Example:

```text
Find and summarize the latest financial
news about Tesla and NVIDIA.
```

---

## ₿ Cryptocurrency Agent

The Crypto Agent uses the **CoinGecko API** to retrieve cryptocurrency prices.

Example:

```text
Fetch the latest price for Bitcoin.
```

---

## 🛒 E-Commerce Agent

The E-Commerce Agent can search for:

* 💰 Product prices
* ⭐ Reviews
* ⚙️ Features
* 🔍 Product information

Example:

```text
Search for the latest reviews and prices
of the iPhone 15.
```

---

## ✈️ Travel Agent

The Travel Agent can search for:

* ✈️ Flights
* 🏨 Hotels
* 💰 Prices
* 📍 Travel information

Example:

```text
Find flight and hotel information for Paris.
```

---

## 🏀 Sports Agent

The Sports Agent searches for the latest sports information and summarizes important:

* 📰 Headlines
* 👤 Player updates
* 🏆 Team updates
* 📢 Sports news

---

## 🛠️ Technologies Used

| Technology       | Purpose            |
| ---------------- | ------------------ |
| 🐍 Python        | Programming        |
| 🤖 Phidata       | AI Agent Framework |
| 🧠 Groq          | LLM                |
| ✨ Gemini         | Generative AI      |
| 🤖 OpenAI        | LLM                |
| 🔎 DuckDuckGo    | Web Search         |
| 📈 Yahoo Finance | Stock Data         |
| ₿ CoinGecko      | Crypto Data        |
| 🌐 Streamlit     | Web Application    |
| 🦙 Ollama        | Local LLM          |
| 🔐 python-dotenv | API Key Management |

---

## 🔐 API Key Security

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
GEMINI_API_KEY=your_gemini_api_key
OPENAI_API_KEY=your_openai_api_key
```

Load environment variables using:

```python
from dotenv import load_dotenv

load_dotenv()
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Swati2064/phidata-ai-agents.git
```

### 2. Navigate to the project

```bash
cd phidata-ai-agents
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install phidata python-dotenv streamlit requests yfinance
```

Install any additional packages required by the individual agents.

---

## ▶️ Running the Project

Run a simple Groq agent:

```bash
python groq_agents.py
```

Run the financial agent:

```bash
python groq_agents1.py
```

Run the multi-agent project:

```bash
python multiagents.py
```

Run the financial analysis:

```bash
python multiagent_financialnew_analysis.py
```

Run the Cricket Gemini application:

```bash
streamlit run cricket_agent_gemini.py
```

Run the Cricket multi-agent application:

```bash
streamlit run cricket_app_agent.py
```

---

## 🧠 Concepts Learned

This project covers:

* Large Language Models
* Prompt Engineering
* AI Agents
* Agentic AI
* Multi-Agent Systems
* Tool Calling
* Web Search
* API Integration
* Financial AI
* Generative AI
* Streamlit Applications
* Environment Variables

---

## 👩‍💻 Author

**Swati Jadhav**

🎓 B.Tech — Artificial Intelligence & Data Science

💡 Interested in:

`Agentic AI` • `Generative AI` • `LLMs` • `Python` • `Machine Learning`

---

<p align="center">
  <b>🤖 Building with AI Agents • Phidata • LLMs • Generative AI</b>
</p>
