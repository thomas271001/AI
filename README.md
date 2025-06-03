# 🤖 Real-Time Face & Emotion Detection

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-enabled-green)
![DeepFace](https://img.shields.io/badge/DeepFace-active-purple)
![MediaPipe](https://img.shields.io/badge/MediaPipe-face--mesh-orange)
![MIT License](https://img.shields.io/badge/license-MIT-yellow.svg)

This repository includes two real-time computer vision applications powered by OpenCV:

- 🎭 **Emotion Detection using DeepFace**
- 👤 **Face Mesh Detection using MediaPipe**

> These applications use your webcam feed to detect and display facial emotions or landmark points in real time.

---

<details>
<summary><strong>📚 Table of Contents</strong></summary>

- [🧠 Project Overview](#-project-overview)
- [📂 Folder Structure](#-folder-structure)
- [⚙️ Installation](#️-installation)
- [🚀 Running the Applications](#-running-the-applications)
- [📸 Sample Output](#-sample-output)
- [❓ Troubleshooting](#-troubleshooting)
- [🤝 Contributing](#-contributing)
- [📝 License](#-license)
</details>

---

## 🧠 Project Overview

### 1. 🎭 Emotion Detection (DeepFace)

Detects and displays the dominant emotion from a user's face using [DeepFace](https://github.com/serengil/deepface).  
✅ Supported emotions: happy, sad, angry, surprise, fear, neutral, disgust.

### 2. 👤 Face Detection (MediaPipe)

Utilizes [MediaPipe FaceMesh](https://google.github.io/mediapipe/solutions/face_mesh.html) to plot 468 facial landmarks for each detected face in the webcam feed.

---

## 📂 Folder Structure

```bash
AI-Vision-Projects/
│
├── emotion_detection.py      # Real-time emotion recognition using DeepFace
├── face_detection.py         # Real-time face landmark detection using MediaPipe
├── requirements.txt
└── README.md
