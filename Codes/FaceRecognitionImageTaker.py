import cv2
import time
from deepface import DeepFace

def main():
    # Open a connection to the webcam
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        print("Error: Could not open video.")
        return

    # Flag and timer initialization
    start_time = time.time()
    image_captured = False
    post_capture_time = None  # Timer for keeping the camera open after capturing

    while True:
        # Read a frame from the webcam
        ret, frame = video_capture.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert frame to RGB format
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        try:
            # Extract faces using DeepFace
            faces = DeepFace.extract_faces(img_path=rgb_frame, detector_backend='opencv')

            if faces:
                for face in faces:
                    facial_area = face['facial_area']

                    # Adjust rectangle coordinates to avoid negative values
                    x = max(facial_area['x'] - int(0.1 * facial_area['w']), 0)
                    y = max(facial_area['y'] - int(0.35 * facial_area['h']), 0)  # Increase y to capture hair
                    w = int(facial_area['w'] + 0.2 * facial_area['w'])  # w + 20%
                    h = int(facial_area['h'] + 0.6 * facial_area['h'])  # h + 60%

                    # Draw a rectangle around the detected face (including hair)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                    # Save a cropped image of the detected face after 1 second
                    if not image_captured and time.time() - start_time > 1:
                        cropped_face = frame[y:y+h, x:x+w]  # Crop the face from the original frame
                        cv2.imwrite('captured_face_with_hair.jpg', cropped_face)  # Save the cropped face image
                        print("Cropped face image captured and saved as 'captured_face_with_hair.jpg'")
                        image_captured = True
                        post_capture_time = time.time()  # Set the time when the image was captured

        except Exception as e:
            print(f"Error in face detection: {e}")

        # Display the frame with detected faces
        cv2.imshow('Video', frame)

        # Check if 2 seconds have passed after capturing the image
        if image_captured and (time.time() - post_capture_time > 2):
            print("Exiting after keeping the camera open for 2 seconds post-capture.")
            break

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
