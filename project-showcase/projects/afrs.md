# AFRS — Autonomous Face Recognition System

> **Edge Computer Vision Pipeline & Automated Biometric Profile Switching.**

---

## 1. Project Overview & Executive Summary

- **System:** AFRS (Autonomous Face Recognition System)
- **Role:** Computer Vision & Systems Engineer
- **Domain:** Edge Computer Vision, Biometric Security, Academic Research
- **Research Citation:** Co-authored research published in *ICEICT* proceedings (Taylor & Francis Group, SCOPUS Index): *"An Implementation of Electronic Device User Profile Switching using Facial Detection"*
- **Status:** Completed Research & Private Engineering Project

AFRS is an edge-based computer vision architecture that automates user desktop environment switching and biometric personalization. Designed for shared terminals and specialized electronic workstations, AFRS detects, aligns, and verifies user identity using facial landmark geometric metrics and embedded deep learning representations without transmitting biometric frames to external servers.

---

## 2. Problem Statement

Electronic devices and shared workstations require rapid, secure user personalization. Legacy authentication mechanisms exhibit significant friction:
1. **Manual Credential Friction:** Requiring repetitive passwords, PINs, or manual account selection slows down operational transitions on shared development machines.
2. **Cloud Biometric Risks:** Offloading facial imagery or biometric templates to cloud databases exposes sensitive personal identity markers to catastrophic security breaches.
3. **Lighting & Pose Sensitivity:** Naive face detection algorithms degrade rapidly under fluctuating ambient lighting, angled facial poses, or partial occlusions.

---

## 3. Goals and Design Constraints

- **Edge-Only Processing:** Facial detection, feature extraction, and identity matching must execute locally on the target machine without network connectivity.
- **Low-Latency Switching:** The complete authentication cycle—from camera frame capture to desktop session trigger—must complete in under 500ms.
- **Pose & Illumination Invariance:** Reliable face alignment across variable yaw, pitch, and roll angles (-30° to +30°).
- **Anti-Spoofing Verification:** Defenses against presentation attacks using static 2D photographs or smartphone displays.

---

## 4. Architecture & Technology Stack

### System Architecture Diagram

```
┌────────────────────────────────────────────────────────┐
│            Live Optical Feed (Edge Webcam)             │
└───────────────────────────┬────────────────────────────┘
                            │ Raw Optical Frame Buffer
                            ▼
┌────────────────────────────────────────────────────────┐
│          Face Detection & Landmark Alignment           │
│   • Multi-task facial landmark extraction (68 points)  │
│   • Affine transformation for geometric normalization  │
└───────────────────────────┬────────────────────────────┘
                            │ Normalized Facial Crop
                            ▼
┌────────────────────────────────────────────────────────┐
│           Feature Extraction & Metric Embedding        │
│          (Deep Metric Representation Engine)           │
│   • 128-dimensional L2-normalized embedding vector     │
└───────────────────────────┬────────────────────────────┘
                            │ Numerical Embedding Vector
                            ▼
┌────────────────────────────────────────────────────────┐
│        Cosine Similarity Metric Matching Engine        │
│   • Compares vector against enrolled local templates   │
│   • Thresholded Euclidean / Cosine verification        │
└───────────────────────────┬────────────────────────────┘
                            │ Authenticated User Identity
                            ▼
┌────────────────────────────────────────────────────────┐
│         Automated OS Profile Switcher Daemon           │
│   • Triggers session configuration & user workspace    │
│   • Immediate frame buffer wipe from system RAM        │
└────────────────────────────────────────────────────────┘
```

### Verified Technology Stack

| Component | Technologies | Implementation Rationale |
| :--- | :--- | :--- |
| **Vision Framework** | OpenCV, C++, Python | Optimized optical frame reading, affine matrix transformations, and image resizing. |
| **Inference Engine** | ONNX Runtime | Low-latency forward passes across edge CPU threads. |
| **Embeddings & Alignment** | Deep Metric Learning, Dlib 68-Point Predictor | Consistent geometric normalization across varied facial poses. |
| **Operating System Bridge** | Linux Session Management / Shell IPC | Native process synchronization and desktop environment activation. |

---

## 5. Important Implementation Details

### Geometric Landmark Alignment
To prevent angle-induced feature degradation, AFRS computes eye coordinates using a 68-point landmark predictor, calculates the angle of inclination, and applies an affine transformation to center and level the eyes horizontally prior to embedding generation.

### Deep Metric Vector Matching
Facial crops are passed through an ONNX-quantized metric network producing a 128-dimensional embedding vector. Recognition is performed by calculating the cosine similarity against enrolled templates, triggering authentication only when the metric passes a strict verification threshold ($\tau = 0.6$).

---

## 6. Engineering Challenges and Solutions

1. **Ambient Lighting Variance:**  
   *Challenge:* Shadows and underexposure caused high rejection rates during evening hours.  
   *Solution:* Integrated adaptive histogram equalization (CLAHE) on the luminance channel, standardizing dynamic range before landmark detection.

2. **Mitigating 2D Photo Presentation Attacks:**  
   *Challenge:* A printed photograph held before the camera could trigger unauthorized profile switching.  
   *Solution:* Integrated a lightweight eye-blink and micro-motion temporal validator requiring dynamic liveliness confirmation before authentication.

---

## 7. Privacy, Reliability, and Security Considerations

- **Ephemerality of Raw Pixels:** Camera frames are retained only in temporary RAM during vector calculation and are immediately wiped.
- **Irreversible Metric Templates:** User identity is represented purely as numerical mathematical vectors; raw biometric imagery is never saved to disk.
- **Local Isolation:** Zero network transmission ensures strict alignment with biometric data privacy standards.

---

## 8. Role and Individual Contributions

- **Computer Vision Engineer:** Yash Gupta co-authored the research, built the OpenCV landmark alignment pipeline, optimized the ONNX inference models, and developed the OS profile switching daemon.
- **Academic Publication:** Co-authored and presented the research published in the *ICEICT* conference proceedings (Taylor & Francis Group, SCOPUS Index).

---

## 9. Current Project Status

- **Status:** Completed Academic Research & Private Engineering Reference.
- **Codebase Status:** Maintained privately as academic intellectual property.

---

## 10. Citation and References

- **Publication:** *"An Implementation of Electronic Device User Profile Switching using Facial Detection"*, International Conference on Electrical, Electronics, Information and Communication Technology (*ICEICT*), published by Taylor & Francis Group (SCOPUS Indexed).
- **Researcher Profile:** [Yash Gupta on GitHub](https://github.com/yashgupta29032006)
