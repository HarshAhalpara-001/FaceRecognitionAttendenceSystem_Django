import cv2
import time
from deepface import DeepFace

def main():
    # Open a connection to the webcam
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        print("Error: Could not open video.")
        return

    # Path to the reference image
    reference_image_path = r'C:\0_DATA\CODE\Face_\Codes\captured_face_with_hair.jpg'  # Use raw string for path

    while True:
        # Read a frame from the webcam
        ret, frame = video_capture.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert frame to RGB format
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        try:
            # Verify the frame against the reference image
            output = DeepFace.verify(img1_path=rgb_frame, img2_path=reference_image_path, enforce_detection=False)
            print(output)

            # Check if verification is successful
            if output['verified']:
                print("Face verified successfully!")
                # Pause for 2 seconds before closing
                time.sleep(2)
                break

        except Exception as e:
            print(f"Error in DeepFace verification: {e}")

        # Display the frame
        cv2.imshow('Video', frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
