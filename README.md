# Yash Gupta

**AI Systems Engineer • Agentic AI • Full-Stack Product Builder**  
Building reliable AI agents, privacy-aware vision systems, and production-oriented software products.

<p align="left">
  <a href="https://www.linkedin.com/in/yash-gupta-554924369"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://github.com/yashgupta29032006"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub" /></a>
  <a href="https://medibridgeai.in"><img src="https://img.shields.io/badge/Live_Product-MediBridge_AI-0284c7?style=flat-square&logo=googlechrome&logoColor=white" alt="MediBridge AI" /></a>
  <a href="https://x.com/YashGupta202927"><img src="https://img.shields.io/badge/X-000000?style=flat-square&logo=x&logoColor=white" alt="X (Twitter)" /></a>
</p>

---

### Executive Profile

I am an AI engineer and systems developer specializing in **multi-agent orchestration**, **intelligent video analytics (IVA)**, and **closed-loop decision systems**. My engineering approach bridges generative reasoning with dependable execution: bounding probabilistic model outputs with deterministic state machines, statistical evaluators, and strict governance barriers.

Currently developing **Rudra 3.0** (an agentic personal assistant and automation framework), engineering **Sentinel AI** (the core vision intelligence model within InvisionAI at Vantage), founding **MediBridge AI** (an intelligent healthcare navigation platform), and architecting **EchoVault** (local-first contextual memory).

---

### Featured Engineering Systems

#### 01. Rudra 3.0 — Personal AI Assistant & Agentic Automation
`Creator & Lead Developer` • *Telegram Protocol Automation & Agent Architecture*  
**Links:** [Rudra App Repository](https://github.com/yashgupta29032006/Rudra_app) • [Architecture Case Study](project-showcase/projects/rudra.md)

- **Problem & Ambient Access:** Developer workflows and research tasks are fragmented across disparate apps; web chatbots lack ambient system access, persistent cross-turn state, and secure execution tools.
- **MTProto Protocol Automation:** Architected an asynchronous Telegram MTProto client via Telethon and Python `asyncio`, enabling natural language task execution and ambient notifications across desktop and mobile.
- **Agent Planning Loop:** Integrated LangChain with Google Gemini API to drive an autonomous planning cycle that dynamically selects tools, evaluates return values, chains multi-step actions, and resolves calendar conflicts.
- **Status & Stack:** Core engine maintained privately; architecture documented in case study. Built with `Python`, `Telethon`, `LangChain`, `Google Gemini API`, `AsyncIO`, and `REST APIs`.

---

#### 02. Sentinel AI — Intelligent Video Analytics
`Lead AI Engineer` • *Privacy-Preserving Edge Computer Vision Model* • **Affiliation:** Vantage (`VantageLLC`)  
**Links:** [Technical Case Study](project-showcase/projects/sentinel-ai.md) • *Source Code Confidential*

- **Problem & Edge Constraints:** Streaming raw surveillance footage to cloud endpoints induces severe network congestion, transmission latency, and civil privacy vulnerabilities.
- **Edge Vision Intelligence:** Developed Sentinel AI as the core intelligent vision perception model within InvisionAI at Vantage, executing spatial-temporal feature extraction and anomaly detection directly on edge nodes.
- **Optimized Model Execution:** Engineered lightweight OpenCV inference pipelines utilizing ONNX Runtime acceleration and facial embedding extraction for real-time processing under constrained compute budgets.
- **Attribution & Confidentiality:** Individual contribution: Sentinel AI vision intelligence model. Collaborative Clawer Bot component developed by teammate Yash Srivastava. Associated with Vantage; source code is proprietary and confidential.

---

#### 03. MediBridge AI — AI-Powered Healthcare Discovery & Navigation
`Founder & Lead Architect` • *Demographically Adaptive Healthcare Navigation Platform*  
**Links:** [Live Platform (medibridgeai.in)](https://medibridgeai.in) • [Case Study](project-showcase/projects/medibridge-ai.md)

- **Problem & Market Disconnect:** Healthcare search across India suffers from predatory advertising bias, opaque consultation costs, and dense digital interfaces that exclude senior citizens and non-technical users.
- **Clinical Specialty Routing:** Engineered an NLP matching engine that maps conversational patient symptom queries directly to relevant medical specialties, clinical urgency levels, and transparent fee schedules.
- **3-Tier Adaptive Interface:** Architected dynamically rendered accessibility modes—*Senior Mode* (high-contrast ratios, 18px+ typography, step-by-step guidance), *Structured Mode*, and *Advanced Mode* with dense comparative data tables.
- **Production Validation:** Deployed live in production at [medibridgeai.in](https://medibridgeai.in); ranks hospitals strictly on verified NABH accreditations and authentic patient feedback with zero sponsored placements. Built with `Next.js (App Router)`, `TypeScript`, and `Tailwind CSS`.

---

#### 04. EchoVault — Personal AI Memory & Agent System
`Systems & Storage Architect` • *Local-First Agent Memory Store & Context Persistence*  
**Links:** [Architecture Case Study](project-showcase/projects/echovault.md) • *Source Code Private*

- **Problem & Privacy Exposure:** AI agents lose contextual state across sessions, while commercial cloud vector databases introduce network latency, recurring expenses, and privacy exposure for sensitive data.
- **Hybrid Local Memory Engine:** Architected a local memory store pairing dense vector embeddings (FAISS) with structured relational storage (SQLAlchemy) for low-latency (<15ms) semantic search and multi-session persistence.
- **Agent Planning & Extensibility:** Developed a modular FastAPI backend providing contextual retrieval, hierarchical memory decay, web research grounding, and calendar integrations wrapped in a Next.js/Electron interface.
- **Zero-Knowledge Boundaries:** Engineered local-at-rest encryption ensuring zero external data egress. Maintained as a private engineering framework; architecture detailed in case study. Built with `Python`, `FastAPI`, `FAISS`, `SQLAlchemy`, `Next.js`, and `Electron`.

---

#### 05. RazorGrowth AI — Autonomous Merchant Growth & Policy-Governed Commerce
`AI Systems Engineer` • *Policy-Governed Commerce & Closed-Loop Experimentation* • **Built for:** Razorpay AI Buildathon 2026  
**Links:** [GitHub Repository](https://github.com/yashgupta29032006/RazorGrowthAI) • **Status:** 415/415 Automated Tests Passing

- **Problem & Authority Governance:** Commercial AI growth tools operate as unconstrained suggestion engines, generating unverified promotional campaigns without margin safety, budget control, or statistical validity.
- **Core Authority Invariant:** Enforced the strict architectural rule: *"AI proposes and explains; deterministic code validates and enforces."*
- **Thompson Sampling & Policy Gate:** Implemented multi-arm bandits with Beta-Bernoulli posteriors and bounded allocation floors (10% floor, 60% cap), governed by an immutable Merchant Policy Gate enforcing margin floors and budget ceilings.
- **Statistical Rigor & Verification:** Built an experimentation lab utilizing FNV-1a sticky cohort hashing, Two-Proportion Z-Tests, and Welch t-Tests. **415/415 automated test suite passing**. Built with `Next.js 15`, `React 19`, `TypeScript`, and `Gemini API`.

---

### Core Technology Stack

<table>
  <tr>
    <td width="28%"><b>AI &amp; Agent Architectures</b></td>
    <td>
      <img src="https://img.shields.io/badge/Gemini_API-8E75C2?style=flat-square&logo=google&logoColor=white" alt="Gemini" />
      <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white" alt="LangChain" />
      <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white" alt="OpenCV" />
      <img src="https://img.shields.io/badge/FAISS-008080?style=flat-square" alt="FAISS" />
      <img src="https://img.shields.io/badge/ONNX_Runtime-005CED?style=flat-square&logo=onnx&logoColor=white" alt="ONNX" />
      <img src="https://img.shields.io/badge/Grounded_RAG-0284c7?style=flat-square" alt="RAG" />
    </td>
  </tr>
  <tr>
    <td><b>Languages &amp; Core</b></td>
    <td>
      <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
      <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
      <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript" />
      <img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white" alt="C++" />
      <img src="https://img.shields.io/badge/SQL-336791?style=flat-square&logo=postgresql&logoColor=white" alt="SQL" />
    </td>
  </tr>
  <tr>
    <td><b>Backend &amp; Protocols</b></td>
    <td>
      <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI" />
      <img src="https://img.shields.io/badge/Telethon-2CA5E0?style=flat-square&logo=telegram&logoColor=white" alt="Telethon" />
      <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=node.js&logoColor=white" alt="Node.js" />
      <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy" />
      <img src="https://img.shields.io/badge/Prisma-2D3748?style=flat-square&logo=prisma&logoColor=white" alt="Prisma" />
    </td>
  </tr>
  <tr>
    <td><b>Frontend &amp; Interface</b></td>
    <td>
      <img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=next.js&logoColor=white" alt="Next.js" />
      <img src="https://img.shields.io/badge/React_19-61DAFB?style=flat-square&logo=react&logoColor=black" alt="React" />
      <img src="https://img.shields.io/badge/Electron-47848F?style=flat-square&logo=electron&logoColor=white" alt="Electron" />
      <img src="https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white" alt="Tailwind" />
      <img src="https://img.shields.io/badge/Recharts-22b5bf?style=flat-square" alt="Recharts" />
    </td>
  </tr>
  <tr>
    <td><b>Cloud, Data &amp; Runtime</b></td>
    <td>
      <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" />
      <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" alt="Redis" />
      <img src="https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white" alt="Supabase" />
      <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite" />
      <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
      <img src="https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white" alt="Vercel" />
    </td>
  </tr>
  <tr>
    <td><b>Guardrails &amp; Experimentation</b></td>
    <td>
      <img src="https://img.shields.io/badge/Thompson_Sampling-38bdf8?style=flat-square" alt="Thompson Sampling" />
      <img src="https://img.shields.io/badge/A/B_Testing-0284c7?style=flat-square" alt="A/B Testing" />
      <img src="https://img.shields.io/badge/Welch_t--Test-14b8a6?style=flat-square" alt="Welch t-Test" />
      <img src="https://img.shields.io/badge/Policy_Gates-6366f1?style=flat-square" alt="Policy Gates" />
    </td>
  </tr>
</table>

---

### GitHub Activity Overview

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=yashgupta29032006&layout=compact&hide_border=true&bg_color=0d1117&title_color=38bdf8&text_color=c9d1d9&hide=qml,c,cython" alt="Most Used Languages" />
</p>

---

### Additional Systems & Research Case Studies

| System | Focus Area | Core Architecture & Engineering Highlights | Status |
| :--- | :--- | :--- | :--- |
| **[CarbonWise AI](https://github.com/yashgupta29032006/CarbonWise-AI)** | ClimateTech Platform | Deterministic grid accounting (US/EU/APAC/Global) + Gemini 2.5 Flash coach & Recharts analytics. | [Live Demo](https://carbonwise-ai.vercel.app) |
| **[PolarisAI](https://github.com/yashgupta29032006/PolarisAI)** | Operational Intelligence | Antarctic station telemetry simulation (Maitri & Bharati), 0–100 risk indexing & load curtailment. | [Repository](https://github.com/yashgupta29032006/PolarisAI) |
| **[AFRS](project-showcase/projects/afrs.md)** | Edge Computer Vision | Autonomous Face Recognition System; landmark alignment, ONNX embeddings & profile switching (ICEICT). | `Source Private` |
| **[CommunityPulse AI](https://github.com/yashgupta29032006/CommunityPulse-AI)** | Civic Decision Systems | Grounded RAG municipal intelligence platform, PulseCopilot explainability logs & Open-Meteo APIs. | [Repository](https://github.com/yashgupta29032006/CommunityPulse-AI) |
| **[AI Shopkeeper](project-showcase/projects/ai-shopkeeper.md)** | Retail Edge Vision | Commodity optical counter tracking, spatial IoU SKU localization & conversational stock inquiry. | `Source Private` |

---

### Connect & Collaborate

Available for technical discussions on agent architectures, edge computer vision, and AI product engineering.

- **LinkedIn:** [linkedin.com/in/yash-gupta-554924369](https://www.linkedin.com/in/yash-gupta-554924369)
- **Product:** [medibridgeai.in](https://medibridgeai.in)
- **GitHub:** [github.com/yashgupta29032006](https://github.com/yashgupta29032006)
- **X (Twitter):** [@YashGupta202927](https://x.com/YashGupta202927)
