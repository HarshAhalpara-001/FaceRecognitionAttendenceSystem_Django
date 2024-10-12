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
