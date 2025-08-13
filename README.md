# Multi-Agent Stock Summary Bot (NVDA Example)

This project demonstrates how to build an **autonomous AI agent team** using [phidata](https://github.com/phidatahq/phidata) to:
1. Search the web for stock-related news.
2. Retrieve analyst recommendations and financial data.
3. Combine results into a neat, markdown-friendly summary.

The example uses **NVDA (NVIDIA)** as the target stock.

---

## Features
- **Two specialized agents**:
  - **Web Search Agent** → Uses DuckDuckGo for the latest news (with sources).
  - **Financial Agent** → Uses Yahoo Finance tools for analyst recommendations, fundamentals, and stock prices.
- **Team Agent** → Combines the above into a single response.
- **Tables and markdown formatting** for clean output.

---

## Setup

### 1. Clone & Install
```bash
git clone <your-repo-url>
cd firstagentic
pip install -r requirements.txt
