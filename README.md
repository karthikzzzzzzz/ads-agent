
## 🧠 Overview

This project implements a lightweight AI agent that performs marketing-relevant research and creative tasks across three core functionalities:

1. Analyze **Google Ads performance CSVs**
2. Retrieve marketing best practices from a **vector database** (Chroma)
3. Rewrite ad copy in a **specific tone**, optimized for a **target platform**

The agent uses **LangGraph** for graph-based orchestration and is served through a **FastAPI** backend. All logic is modular and extensible for use in real-world marketing workflows.

---

## 🧱 1. Architecture and Tools Used

The solution is architected as a **multi-step agent** using LangGraph and LangChain components. Each processing step is a node in a LangGraph `StateGraph`. The system is exposed via a `POST /run-agent` route through FastAPI.

### Core Tools:
- `LangGraph`: Multi-step agent orchestration
- `LangChain`: LLM orchestration and retrieval
- `ChatOpenAI (GPT-4)`: Language model
- `Chroma`: Local vector database for marketing blogs
- `FastAPI`: Backend serving layer
- `rouge-score` + `ragas`: Evaluation tools for summarization and retrieval

---

## 🔁 2. Use of Agentic RAG

This solution implements **Agentic RAG**, where each reasoning step is an agent node in the workflow. For example:

- CSV insight generation is performed using a prompt-aware GPT-4 agent
- Retrieved marketing blogs are injected into the rewrite process
- Past mistakes (e.g., hallucination) affect prompt tuning via memory

This graph-based design allows **multi-hop reasoning** and improves **traceability**, **modularity**, and **precision** compared to linear pipelines.

---

## 🧠 3. Knowledge Graph Integration (Future Scope)

Though not implemented in the prototype, a **Knowledge Graph (KG)** can improve context relevance. For example:

- `Ad → has_metric → CTR`
- `Creative → suited_for → Instagram`
- `UserIntent → influenced_by → Copy Tone`

KG relationships could power semantic reasoning, filtering of retrieved content, and entity-grounded copy rewriting using LangChain’s KG tools or Neo4j.

---

## 📊 4. Evaluation Strategy

We use both **manual** and **automated** evaluation:

### Metrics:
- **ROUGE-L**: Measures similarity between original and rewritten ad copy
- **RAGAS**: Evaluates retrieval quality (faithfulness, answer relevance, etc.)
- **F1 Score**: (Optional) for performance metric extraction from CSV
- **Hallucination Rate**: Manually checked or flagged in logs

This combination ensures high-quality, trustworthy agent responses.

---

## 🔄 5. Pattern Recognition and Improvement Loop

A **memory feedback node** stores prior errors (e.g., hallucinations). When triggered, it modifies prompt structure or adjusts control flow.

Future improvements:
- LangGraph's memory nodes with `StateHistory`
- Prompt refiners based on RAGAS scores
- Feedback embedding DBs for long-term learning

---

## 🌐 6. Integration with Meta Business Manager

While this version focuses on Google Ads data, the agent is easily extendable to work with **Meta Business Manager** via **Meta Cloud Marketing APIs**. These APIs provide access to:

- Campaign insights
- Creative performance
- Targeting data

This data can be fetched and passed into the same CSV pipeline, allowing unified analysis and rewrite suggestions across both ad ecosystems.

---

## 📈 7. Improving the Agent’s Responses

To further enhance the agent:
- Use **dynamic prompt templates** based on campaign objective
- Add **few-shot examples** to the ad rewrite node
- Include retrieved blog examples in the LLM context
- Add **retrieval rerankers** to improve vector recall quality
- Route input via **intent classifier** (e.g., performance query vs copywriting)

---

## ⚙️ 8. Detailed Workflow

```mermaid
graph TD
    A[User Uploads CSV + Ad Text] --> B[Analyze CSV via GPT-4]
    B --> C[Retrieve Relevant Blog Posts (Chroma)]
    C --> D[Rewrite Ad Copy (tone, platform)]
    D --> E[Feedback Node (prior errors)]
    E --> F[Evaluate Output (ROUGE, RAGAS)]
    F --> G[Return Insights + Rewritten Copy]
```

## How to run

Load the env variables with the keys for the openai or use ollama models via ChatOpenAI

pip install -r requirements.txt
uvicorn app.main:app --reload
