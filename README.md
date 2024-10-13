
```markdown
# Face Detection and Verification System

This project demonstrates a real-time face detection and verification system using Python, OpenCV, and the DeepFace library. The application captures images from the webcam, detects faces, and verifies them against a reference image.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
  - [Face Detection and Image Capture](#1-face-detection-and-image-capture)
  - [Face Verification](#2-face-verification)
- [Notes](#notes)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Author](#author)

## Features

- **Face Detection:** Detects faces in real-time from the webcam feed and draws a bounding box around them.
- **Image Capture:** Captures and saves a cropped face image (including hair) after detecting a face.
- **Face Verification:** Verifies the detected face in real-time against a pre-saved reference image.
- **Customizable Detection Parameters:** Easily adjustable bounding box settings for face and hair detection.

## Technologies Used

- **Python**
- **OpenCV:** For real-time image processing and camera operations.
- **DeepFace:** A Python library for facial recognition and analysis.

## Prerequisites

Ensure you have the following libraries installed:

- Python 3.6+
- OpenCV: Install using the command:
  ```bash
  pip install opencv-python
  ```
- DeepFace: Install using the command:
  ```bash
  pip install deepface
  ```

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/face-detection-verification.git
   cd face-detection-verification
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Save a reference image in the path specified within the code or update the path in the script to point to your reference image.

## Usage

### 1. Face Detection and Image Capture

Run the following command to start the webcam and detect faces:
```bash
python face_detection.py
```

- The application captures an image after detecting a face for more than 1 second and saves it as `captured_face_with_hair.jpg`.
- It keeps the camera open for 2 seconds post-capture before closing.

### 2. Face Verification

To verify the captured face against the reference image, run:
```bash
python face_verification.py
```

- The script continuously verifies the detected face against the reference image.
- If a match is found, the system confirms the verification and closes after a 2-second pause.

### Keyboard Controls

- Press `q` to exit the webcam feed manually at any time.

## Notes

- Make sure your webcam is functioning properly.
- The path to the reference image should be updated to match your setup.
- Adjust the detection settings (such as the bounding box for face and hair) according to your requirements.

## Troubleshooting

- If the webcam feed doesn’t open, ensure the camera is connected and accessible.
- For detection issues, verify that the `DeepFace` library is correctly installed and configured.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Harsh Ahalpara**  
- [GitHub](https://github.com/HarshAhalpara-001)  
- [LinkedIn](https://www.linkedin.com/in/harsh-ahalpara-055027252/)

## Functions Overview

### 1. `main()`
The main function handles the webcam feed, captures images, and processes facial detection and verification. Key steps include:

- **Opening the Webcam:** Initializes the video capture from the webcam.
- **Reading Frames:** Continuously reads frames from the webcam.
- **Face Detection:** Uses the DeepFace library to extract faces from each frame.
- **Bounding Box Drawing:** Draws a rectangle around detected faces, adjusted to capture hair.
- **Image Saving:** Captures and saves a cropped image of the detected face after a specified time.
- **Face Verification:** Verifies the captured face against a reference image in a separate function.

### Libraries Used

- **OpenCV (`cv2`)**: Utilized for video capture, frame processing, and drawing on frames.
- **DeepFace**: Provides functionalities for facial detection and verification.

### Key Operations

- **Face Detection and Image Capture**: Involves initializing the webcam, detecting faces, and saving the image when a face is detected.
- **Face Verification**: Compares the live video feed with a stored reference image to confirm identity.

---
