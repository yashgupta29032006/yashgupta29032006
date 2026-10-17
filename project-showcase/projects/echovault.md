# EchoVault — Personal AI Memory & Agent System

> **A Local-First Agent Memory & Context Store with Tool Execution & Cross-Session Persistence.**

---

## 1. Project Overview & Executive Summary

- **System:** EchoVault
- **Role:** Systems & Storage Architect
- **Project Classification:** Private Engineering Framework
- **Status:** Active Evolution • Proprietary Core Architecture
- **Domain:** Local-First Software, Vector Similarity Retrieval, Persistent AI Memory, Hybrid Relational-Vector Stores

EchoVault is an intelligent, local-first memory and context-persistence system engineered for autonomous agents and developer workflows. It resolves the fundamental limitation of conversational AI—session amnesia—by coupling a sub-15ms local vector similarity search engine (FAISS) with structured relational metadata storage (SQLAlchemy/SQLite). Encapsulated within a modular FastAPI backend and accessible via an Electron and Next.js desktop interface, EchoVault empowers AI agents to recall historical knowledge, maintain long-term user context, and invoke local tools without leaking private data to cloud vector databases.

---

## 2. Problem Statement

Modern conversational agents and multi-agent workflows encounter severe operational bottlenecks when managing long-term memory:
1. **Third-Party Cloud Privacy Exposure:** Storing personal notes, proprietary code snippets, and confidential conversation embeddings on commercial vector-as-a-service platforms introduces severe privacy vulnerabilities and potential data leakage.
2. **Context Fragmentation & Session Amnesia:** Most AI agents reset their cognitive state after a session terminates. They cannot recall historical decisions, ongoing project requirements, or evolving user preferences.
3. **Decoupled Tool Execution:** Standard Retrieval-Augmented Generation (RAG) tools retrieve static text fragments but lack the cognitive scaffolding to link retrieved memory into active tool execution pipelines (such as automated web research, task scheduling, or calendar management).

---

## 3. Goals and Design Constraints

- **Absolute Local-First Privacy:** Zero external data egress for memory embeddings or relational schemas. All embeddings and databases must reside strictly on the local host filesystem.
- **Sub-15ms Retrieval Latency:** Ultra-fast vector similarity queries over thousands of memory embeddings without depending on internet round-trips.
- **Hybrid Storage Architecture:** Tight synchronization between dense vector representations (similarity search) and relational metadata (timestamps, category tags, session IDs, access counts).
- **Graceful Memory Decay & Relevance Scoring:** Dynamic weighting that balances semantic similarity with temporal recency, preventing outdated instructions from overriding recent context.
- **Cross-Platform Desktop Accessibility:** A desktop client (Electron + Next.js) enabling real-time memory inspection, semantic search debugging, and agent thought-stream visualization.

---

## 4. Architecture & Technology Stack

### System Architecture Diagram

```
┌────────────────────────────────────────────────────────┐
│             Desktop Interface Layer                    │
│             (Next.js + Electron UI)                    │
│   • Context manager & memory inspection canvas         │
│   • Real-time agent thought logs & query console       │
└───────────────────────────┬────────────────────────────┘
                            │ Local IPC / HTTP REST
                            ▼
┌────────────────────────────────────────────────────────┐
│            FastAPI Memory & Agent Core Daemon          │
│   ├── Query Preprocessor & Embedding Generator         │
│   ├── Hybrid Retrieval Coordinator                     │
│   └── Multi-Step Agent Tool Planner (Gemini API)       │
└───────────────┬────────────────────────┬───────────────┘
                │                        │
    ┌───────────┴──────────┐   ┌─────────┴─────────────┐
    ▼                      ▼   ▼                       ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────────────────┐
│ Vector Engine │ │Relational Meta│ │     Modular Tools         │
│ (FAISS Index) │ │ (SQLAlchemy / │ │ • Web Research Scraper    │
│ • Dense metric│ │  SQLite DB)   │ │ • Calendar Sync & Events  │
│   search      │ │ • Session IDs │ │ • Task & Reminder Dispatch│
│ • <15ms search│ │ • Temporal tag│ └───────────────────────────┘
└───────────────┘ └───────────────┘
```

### Verified Technology Stack

| Layer | Technologies | Rationale |
| :--- | :--- | :--- |
| **Backend & Orchestration** | Python 3.10+, FastAPI, Uvicorn | High-performance asynchronous API layer with automatic OpenAPI documentation. |
| **Vector Engine** | FAISS (Facebook AI Similarity Search), SentenceTransformers | Hardware-optimized vector similarity indexing running entirely in local memory. |
| **Relational Storage** | SQLAlchemy, SQLite | Zero-configuration, serverless relational database managing complex metadata and foreign-key constraints. |
| **AI Planning Core** | Google Gemini API | Structured function calling, context synthesis, and agentic multi-step planning. |
| **Desktop Client** | Next.js, React, Electron, Tailwind CSS | Cross-platform desktop application packaging native OS window management with reactive web UI. |

---

## 5. Important Implementation Details

### Hybrid Vector-Relational Coordination
EchoVault maintains a synchronized mapping between two disparate storage engines:
1. **FAISS Vector Index:** Stores dense floating-point embeddings representing user messages, research findings, and task notes. Query vectors return top-$k$ nearest neighbors within milliseconds.
2. **SQLAlchemy Relational Database:** Uses the vector integer IDs as primary keys to join with relational tables storing creation timestamps, last-accessed timestamps, project scopes, importance weights, and decay factors.

### Temporal Memory Decay Algorithm
EchoVault applies a hybrid relevance scoring formula:
$$\text{Score} = \alpha \cdot \text{CosineSimilarity} + (1 - \alpha) \cdot e^{-\lambda \cdot \Delta t}$$
where $\Delta t$ represents elapsed time since last access, ensuring that actively referenced project memories remain prioritized over stale information.

### Agent Tool Chaining & Synthesis
When an incoming query demands real-world action, the FastAPI backend retrieves relevant background memories, feeds them as grounding context into the Gemini planning engine, and executes verified tool invocations (e.g., creating calendar events or conducting web research) before returning a synthesized result.

---

## 6. Engineering Challenges and Solutions

1. **Synchronizing FAISS Indexes with Relational Mutations:**  
   *Challenge:* FAISS indexes are memory-mapped arrays that do not inherently support transactional row updates or arbitrary deletions.  
   *Solution:* Implemented an event-driven sync manager that marks deleted records in SQLite with a soft-delete tombstone and periodically rebuilds the compact FAISS index during idle system intervals.

2. **Managing Local Memory Footprint in Electron:**  
   *Challenge:* Running an Electron client alongside Python FastAPI and a vector embedding model risked high RAM consumption on developer machines.  
   *Solution:* Decoupled the Python core into an on-demand background daemon and quantized the local embedding model, capping baseline memory usage under 350MB.

3. **Context Window Saturation in LLM Invocations:**  
   *Challenge:* Naively dumping all retrieved memory chunks into the prompt exceeded token limits and caused reasoning degradation.  
   *Solution:* Integrated a semantic deduplication step that filters out overlapping memory fragments, selecting only the top-ranked, mutually distinct context chunks.

---

## 7. Privacy, Reliability, and Security Considerations

- **Local Storage Invariant:** All SQLite databases, vector index files, and configuration stores reside strictly in the user's local application data directory.
- **No Cloud Vector Leakage:** Unlike SaaS vector platforms, no raw text embeddings or personal identity markers are ever transmitted to third-party databases.
- **Sandboxed Tool Operations:** System scripts and file-writing utilities operate within designated project directories to eliminate inadvertent overwrites.

---

## 8. Role and Individual Contributions

- **Sole Architect & Systems Engineer:** Yash Gupta conceptualized and engineered the full EchoVault system.
- **Storage Engineering:** Built the dual FAISS-SQLAlchemy synchronization layer and hybrid decay algorithms.
- **API & Backend:** Developed the FastAPI server, endpoint routers, and tool execution orchestration.
- **Desktop Client:** Designed and built the Next.js and Electron desktop application interface.

---

## 9. Current Project Status

- **Status:** Private Engineering Framework.
- **Repository Visibility:** Maintained as a private repository for ongoing agentic research and personal knowledge management.
- **Evolution:** Currently experimenting with graph-based relational entity links for multi-agent shared memory.

---

## 10. Links and Reference Documentation

- **Architecture Documentation:** [Sanitized Case Study Index](../README.md)
- **Profile Portfolio:** [Yash Gupta on GitHub](https://github.com/yashgupta29032006)
- **Developer Inquiries:** [LinkedIn Profile](https://www.linkedin.com/in/yash-gupta-554924369)
