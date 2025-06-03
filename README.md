
# Real-Time Face & Emotion Detection

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![DeepFace](https://img.shields.io/badge/DeepFace-0.0.75-orange)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.8.10-yellow)
![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey)

This repository contains real-time computer vision applications powered by OpenCV:

- **Emotion Detection** using DeepFace
- **Face Mesh Detection** using MediaPipe

> These applications utilize your webcam feed to detect and display facial emotions or landmark points in real time.

---

## 📁 Folder Structure

```
├── Emotion_Detection.py       # Real-time emotion detection using DeepFace
├── Face_Detection.py          # Real-time face mesh detection using MediaPipe
├── Sign_lang_Detection.py     # Sign language detection script
├── hand_distance.py           # Hand distance measurement script
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## ⚙️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/thomas271001/AI.git
   cd AI
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Running the Applications

### 1. Emotion Detection

Utilizes DeepFace for real-time emotion recognition.

```bash
python Emotion_Detection.py
```

### 2. Face Mesh Detection

Leverages MediaPipe for detecting facial landmarks.

```bash
python Face_Detection.py
```

### 3. Sign Language  Detection

Leverages MediaPipe for detecting Sign Language .

```bash
python Sign_lang_Detection.py
```

### 4. Hand Distance From Camera Detection

Leverages MediaPipe for detecting Hand Distance from camera.

```bash
python Hand_Distance.py
```

> Ensure your webcam is connected and accessible.

---

## ❓ Troubleshooting

- **Webcam Not Detected:**
  - Ensure no other application is using the webcam.
  - Check if the correct camera index is used in the script.

- **Slow Performance:**
  - Close unnecessary applications to free up system resources.
  - Consider reducing the resolution of the video feed in the script.

- **Module Import Errors:**
  - Verify that all dependencies are installed correctly.
  - Reinstall the requirements:

    ```bash
    pip install --upgrade --force-reinstall -r requirements.txt
    ```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature/YourFeature
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add YourFeature"
   ```

4. Push to the branch:

   ```bash
   git push origin feature/YourFeature
   ```

5. Open a pull request.

---


## 📬 Contact

For any inquiries or feedback, please contact [thomas271001](https://github.com/thomas271001).
