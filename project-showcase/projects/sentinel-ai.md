# Sentinel AI — Core Model of InvisionAI

> **A Distributed, Privacy-Preserving Intelligent Video Analytics (IVA) Architecture for Proactive Urban Intelligence.**

---

## 1. Project Overview & Executive Summary

- **Model / System:** Sentinel AI (Core Vision Perception Model of InvisionAI)
- **Role:** Lead AI & Computer Vision Systems Engineer
- **Parent Platform:** InvisionAI
- **Affiliation:** Vantage (`VantageLLC`)
- **Status:** Proprietary Production Architecture • Private Repository
- **Domain:** Intelligent Video Analytics (IVA), Edge Computer Vision, Anomaly Detection, Privacy Engineering

Sentinel AI was engineered as the primary vision perception model within **InvisionAI**, a distributed urban intelligence and surveillance analytics ecosystem developed at **Vantage** (`VantageLLC`). Sentinel AI deploys directly onto resource-constrained edge computing nodes to execute real-time video analytics, spatial-temporal anomaly detection, and facial feature extraction locally. By processing visual data at the edge and discarding raw video immediately after numerical vectorization, Sentinel AI provides security intelligence while mathematically preventing unauthorized surveillance data leakage.

---

## 2. Problem Statement

Conventional urban video surveillance architectures rely on streaming continuous camera footage back to centralized cloud data centers. This paradigm suffers from three critical architectural flaws:
1. **Severe Privacy Infringements:** Continuous transmission and long-term cloud storage of unredacted high-resolution public camera feeds violate civilian privacy regulations and expose sensitive citizen movements to centralized database leaks.
2. **Bandwidth & Latency Chokepoints:** Streaming concurrent multi-camera 1080p/4K streams rapidly saturates local uplinks and induces multi-second transmission latencies, rendering real-time intervention during fast-evolving safety incidents impossible.
3. **Passive & Reactive Monitoring:** Legacy security centers rely heavily on passive human monitors or post-incident video scrubbing rather than proactive, automated anomaly detection at the instant of occurrence.

---

## 3. Goals and Design Constraints

- **Edge-Only Inference:** All neural perception, object localization, and feature extraction must execute locally on edge camera hardware or on-premise edge gateways without dependent cloud connectivity.
- **Zero Raw Video Egress:** Raw pixel streams must never leave the local edge node. Only cryptographically verified, anonymized event vectors and numerical metadata may be transmitted upstream.
- **Real-Time Framerate Budget:** The computer vision pipeline must sustain predictable inference speeds (20–30 FPS) on embedded x86/ARM processors without requiring high-power datacenter GPUs.
- **Robustness Under Challenging Visual Conditions:** Reliable detection despite fluctuating diurnal lighting, camera sensor noise, optical occlusions, and varied angles of incidence.
- **Strict Decoupling of Services:** A modular micro-service architecture separating perception from subsequent crawling, storage, and notification subsystems.

---

## 4. Architecture & Technology Stack

### System Architecture Diagram

```
┌────────────────────────────────────────────────────────┐
│             Edge Video Sensor / CCTV Feed              │
│               (RTSP / Local Camera Bus)                │
└───────────────────────────┬────────────────────────────┘
                            │ Raw Video Stream (Local Device Memory)
                            ▼
┌────────────────────────────────────────────────────────┐
│          Frame Preprocessing & Spatial Normalization   │
│           (OpenCV • Python / C++ High-Speed I/O)       │
│   • Motion mask generation & background subtraction    │
│   • Optical flow normalization & sensor noise filtering│
└───────────────────────────┬────────────────────────────┘
                            │ Normalized Tensors
                            ▼
┌────────────────────────────────────────────────────────┐
│            Sentinel AI Edge Inference Engine           │
│                  (ONNX Runtime Model)                  │
│   ├── Spatial-Temporal Anomaly Detection               │
│   ├── Object & Entity Localization                     │
│   └── Biometric Metric Feature Vectorization           │
└───────────────────────────┬────────────────────────────┘
                            │ (Raw Video Discarded From RAM)
                            │ Anonymized Numerical Vectors & Tokens
                            ▼
┌────────────────────────────────────────────────────────┐
│         Cryptographic Event Tokenizer & IPC            │
│   • Generates cryptographically hashed event records   │
│   • Zero visual pixels retained                        │
└───────────────────────────┬────────────────────────────┘
                            │ Event Metadata via Local IPC
                            ▼
┌────────────────────────────────────────────────────────┐
│         InvisionAI Coordinator & Downstream Agents     │
│   ├── Clawer Bot (Automated Event Web Crawler)         │
│   └── Vantage Proactive Intelligence Dashboard        │
└────────────────────────────────────────────────────────┘
```

### Verified Technology Stack

| Component | Technologies | Implementation Rationale |
| :--- | :--- | :--- |
| **Computer Vision Core** | OpenCV, NumPy, C++ | High-performance frame acquisition, optical flow normalization, and bounding box operations. |
| **Model Runtime** | ONNX Runtime | Hardware-accelerated inference across heterogeneous edge architectures without heavy CUDA runtime baggage. |
| **Perception Framework** | Intelligent Video Analytics (IVA), Face Embeddings | Compact mathematical representations capturing spatial-temporal motion patterns without storing visual pixels. |
| **Edge Communication** | ZeroMQ / Local IPC, RESTful JSON Schemas | Ultra-low latency inter-process messaging between Sentinel AI and companion service daemons. |
| **Runtime Environment** | Linux Containerization, Embedded x86/ARM | Predictable, reproducible edge node deployments under constrained thermal envelopes. |

---

## 5. Important Implementation Details

### Spatial-Temporal Feature Extraction Pipeline
Sentinel AI decomposes video streams into consecutive temporal windows. Using optical flow algorithms and lightweight convolutional backbones optimized into ONNX formats, the model extracts spatial-temporal feature tensors that describe velocity, direction, and interaction dynamics within monitored zones.

### Hardware-Accelerated Quantized Inference
To operate within strict compute envelopes, the model graphs were converted and quantized to 8-bit integers (INT8) using ONNX Runtime. This reduced memory footprint significantly, enabling sustained multi-stream analysis on edge hardware without thermal throttling.

### Strict Privacy-Preserving Mathematical Vectorization
Immediately upon frame ingestion and tensor calculation:
1. Behavioral patterns and facial geometries are transformed into abstract mathematical embedding vectors.
2. The original raw video frame buffer is immediately overwritten in memory.
3. Only the non-invertible numerical vectors, bounding coordinate boxes, timestamp, and anomaly scores are transmitted to downstream services.

---

## 6. Engineering Challenges and Solutions

1. **Inference Latency on Low-Power Edge Devices:**  
   *Challenge:* Full-precision neural models overwhelmed local CPU pipelines, causing frame-buffer backlog and multi-second lag.  
   *Solution:* Implemented dynamic frame skipping based on motion thresholds, combined with INT8 model quantization via ONNX Runtime, preserving real-time performance (>24 FPS) on local hardware.

2. **False Positives from Environmental Noise:**  
   *Challenge:* Wind-blown foliage, shadows, and camera lens flare generated spurious anomaly alerts in initial test runs.  
   *Solution:* Integrated spatial region-of-interest (ROI) masking and temporal verification windows, requiring an anomaly signature to persist across consecutive frames before firing an event trigger.

3. **Inter-Service Decoupling:**  
   *Challenge:* Synchronous coupling between video perception and alert dispatch caused camera dropped frames whenever downstream networks stalled.  
   *Solution:* Designed an asynchronous message-passing queue using lightweight IPC, ensuring Sentinel AI continues uninterrupted frame analysis regardless of network or crawler status.

---

## 7. Privacy, Reliability, and Security Considerations

- **Privacy-by-Design Compliance:** Designed from the ground up to respect global privacy standards (including GDPR Article 25 data protection by design). Raw video never traverses external networks or lands on physical storage disks.
- **Cryptographic Event Authenticity:** Alert payloads are signed with local device keys to prevent spoofing or injection of fabricated security alerts.
- **Fault-Tolerant Edge Watchdogs:** Deployed with lightweight process supervisors that monitor memory usage and automatically recover pipelines in the event of camera driver resets.

---

## 8. Role, Attribution & Collaboration

> **Individual Contribution:**  
> **Yash Gupta:** Conceptualized, architected, and programmed the **Sentinel AI** vision perception model, edge inference pipeline, OpenCV/ONNX optimization, and inter-process communication schemas.
>
> **Collaborative Component:**  
> **Clawer Bot:** Developed by teammate **Yash Srivastava**. Clawer Bot acts as an automated event crawler and workflow agent that consumes upstream alerts generated by Sentinel AI.
>
> **Parent Organization:**  
> InvisionAI is an engineering project associated with the **Vantage** organization (`VantageLLC`).

---

## 9. Current Project Status

- **Status:** Proprietary Production Architecture.
- **Repository Visibility:** Private repository under VantageLLC.
- **Codebase Access:** Source code, proprietary model architectures, and trained weights remain strictly confidential under organizational intellectual property agreements.

---

## 10. Verification & Technical Inspection Policy

Due to intellectual property and security agreements with Vantage (`VantageLLC`), the raw source code and trained weights for Sentinel AI are **not publicly hosted**. 

However, mathematical formulations, high-level system diagrams, optimization trade-offs, and edge deployment paradigms are documented here and available for technical discussion during formal engineering interviews.

- **Developer Profile:** [Yash Gupta on GitHub](https://github.com/yashgupta29032006)
- **Professional Contact:** [LinkedIn Profile](https://www.linkedin.com/in/yash-gupta-554924369)
