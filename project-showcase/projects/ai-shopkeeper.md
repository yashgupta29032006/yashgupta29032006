# AI Shopkeeper — Technical Case Study

> **Edge Computer Vision SKU Detection, Real-Time Cart State Tracking & Automated Billing Intelligence.**

---

## 1. Project Overview & Executive Summary

- **System:** AI Shopkeeper
- **Role:** Lead AI & Full-Stack Systems Developer
- **Project Classification:** Private Engineering Project
- **Status:** Functional Prototype • Maintained Privately
- **Domain:** Retail Edge Vision, Object Detection, Real-Time Cart Tracking, Point-of-Sale (POS) Systems

AI Shopkeeper is a computer vision and conversational billing platform designed to make frictionless checkout accessible to small and medium retail merchants. Operating on commodity webcams and standard x86/ARM hardware, the system detects retail items, tracks dynamic cart state changes via spatial bounding box transitions, and provides a hands-free conversational voice interface for inventory inquiries and automated billing.

---

## 2. Problem Statement

Small-to-medium retail establishments face significant operational and economic bottlenecks:
1. **Checkout Delays:** Manual barcode scanning during peak shopping hours leads to customer congestion and cart abandonment.
2. **Inventory Shrinkage:** Discrepancies between physical shelf movement and POS registry tallies cause undetected stock loss.
3. **Prohibitive Hardware Costs:** Enterprise "frictionless checkout" solutions require multi-camera ceiling grids and expensive datacenter GPU servers that are financially inaccessible to standard shopkeepers.

---

## 3. Goals and Design Constraints

- **Commodity Hardware Support:** Run real-time detection and state tracking on affordable single-webcam setups and standard desktop CPUs.
- **Accurate SKU Identification:** Real-time object classification and bounding box localization across varied packaging orientations.
- **Deterministic Cart Transitions:** Prevent duplicate billing or missed items using spatial Intersection over Union (IoU) state boundaries.
- **Low-Latency Billing Updates:** Instantaneous (<100ms) UI updates upon item placement in the active checkout zone.

---

## 4. Architecture & Technology Stack

### System Architecture Diagram

```
┌────────────────────────────────────────────────────────┐
│            Counter Webcam Optical Feed (USB)           │
└───────────────────────────┬────────────────────────────┘
                            │ Real-Time Video Frames
                            ▼
┌────────────────────────────────────────────────────────┐
│            Edge Object Detection Pipeline              │
│               (YOLO / MobileNet Backbones)             │
│   • Multi-class retail SKU localization                │
│   • Bounding box coordinate regression                 │
└───────────────────────────┬────────────────────────────┘
                            │ Object Coordinates & Class Confidences
                            ▼
┌────────────────────────────────────────────────────────┐
│       Spatial Cart State Machine & IoU Tracker         │
│   • Tracks entry into delimited "Bagging Zone"         │
│   • Prevents duplicate tallies using spatial hysteresis│
└───────────────────────────┬────────────────────────────┘
                            │ Validated Item Events
                            ▼
┌────────────────────────────────────────────────────────┐
│          Dynamic Billing Core & POS Dashboard          │
│   ├── Real-time subtotal tally & itemized registry     │
│   └── Conversational Voice Assistant (Gemini API / STT)│
└────────────────────────────────────────────────────────┘
```

### Verified Technology Stack

| Layer | Technologies | Rationale |
| :--- | :--- | :--- |
| **Vision & Detection** | Python, OpenCV, YOLOv8 / MobileNet | Efficient object localization optimized for real-time edge processing. |
| **Backend & Streams** | FastAPI, WebSockets | Low-latency binary video streaming and bidirectional cart updates. |
| **NLP & Voice** | Google Gemini API, Local STT | Natural language speech interaction for hands-free merchant inventory queries. |
| **Frontend** | Modern Web Interface, HTML5 Canvas | Real-time bounding box visualization and instant digital receipt rendering. |

---

## 5. Important Implementation Details

### Spatial Hysteresis & IoU Cart Logic
To eliminate duplicate item increments, the checkout counter is segmented into visual zones (e.g., "Scanning Zone" and "Bagged Zone"). The system requires an item’s bounding box centroid to cross the boundary and sustain an Intersection over Union (IoU) overlap within the bagging zone for at least three consecutive frames before triggering an immutable billing event.

### Conversational Inventory Assistant
Integrated with Google Gemini API, allowing merchants or customers to make natural voice inquiries (e.g., "What is the total price?", "Do we have more almond milk in stock?") without touching the screen.

---

## 6. Engineering Challenges and Solutions

1. **Handling Occlusion on Crowded Counters:**  
   *Challenge:* Items partially occluding one another led to temporary bounding box drops.  
   *Solution:* Integrated Kalman filter state tracking to preserve item identity trajectories during temporary visual occlusions.

2. **Low-Compute CPU Optimization:**  
   *Challenge:* Sustaining 25+ FPS without dedicated discrete GPUs.  
   *Solution:* Applied model pruning and ONNX quantization to the object detection backbone, reducing memory overhead and CPU cycle consumption.

---

## 7. Privacy, Reliability, and Security Considerations

- **Customer Anonymity:** The optical feed strictly monitors the checkout counter plane; customer facial features are outside the region-of-interest and are never recorded.
- **Local Transaction Integrity:** Cart registries are stored locally in transactional SQLite tables with unique item hashes to prevent duplicate invoice generation.

---

## 8. Role and Individual Contributions

- **Sole Developer:** Yash Gupta developed the complete AI Shopkeeper system, including the computer vision detection pipeline, spatial cart state machine, FastAPI WebSockets server, and POS dashboard.

---

## 9. Current Project Status

- **Status:** Functional Engineering Prototype.
- **Visibility:** Maintained privately as an experimental edge vision retail prototype.

---

## 10. Links and Reference Documentation

- **Architecture Documentation:** [Sanitized Case Study Index](../README.md)
- **Profile Portfolio:** [Yash Gupta on GitHub](https://github.com/yashgupta29032006)
- **Developer Inquiries:** [LinkedIn Profile](https://www.linkedin.com/in/yash-gupta-554924369)
