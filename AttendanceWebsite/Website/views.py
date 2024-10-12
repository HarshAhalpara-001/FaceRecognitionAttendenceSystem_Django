from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import cv2
import numpy as np
import time
from deepface import DeepFace
from .forms import StudentForm
from .models import StudentImage
from django.conf import settings
import os


# View to test if the server is running
def hello(request):
    return HttpResponse("Hello")

# Render the webcam view
def webcam_view(request):
    return render(request, 'webcam.html')

# View to handle student form submission and proceed to face verification
def student_form_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the student data to the database
            student = form.save(commit=False)
            student.save()
            
            # Proceed to verify the face after form submission
            return verify_face(request, student)
    else:
        form = StudentForm()

    return render(request, 'students_form.html', {'form': form})

@csrf_exempt  # Disable CSRF validation for simplicity (adjust for production)
def verify_face(request, student):
    if request.method == 'POST':
        # Open a connection to the webcam
        video_capture = cv2.VideoCapture(0)

        if not video_capture.isOpened():
            return JsonResponse({'error': 'Could not open video.'}, status=500)

        # Initialize the start time and flags
        start_time = time.time()
        image_captured = False
        post_capture_time = None  # Timer for keeping the camera open after capturing

        while True:
            # Read a frame from the webcam
            ret, frame = video_capture.read()
            if not ret:
                video_capture.release()
                return JsonResponse({'error': 'Could not read frame.'}, status=500)

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
                            image_filename = f"{student.class_name}_{student.division}_{student.roll_no}_face.jpg"
                            cropped_face = frame[y:y+h, x:x+w]  # Crop the face from the original frame

                            # Define the path where the image will be saved
                            save_path = os.path.join(settings.MEDIA_ROOT, 'student_images', image_filename)
                            os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Create directories if they don't exist

                            # Save the cropped face image
                            cv2.imwrite(save_path, cropped_face)
                            print(f"Cropped face image captured and saved as '{save_path}'")
                            
                            # Update the student record with the image path and save it to the database
                            student.image = f'student_images/{image_filename}'
                            student.save()
                            
                            image_captured = True
                            post_capture_time = time.time()  # Set the time when the image was captured

            except Exception as e:
                print(f"Error in face detection: {e}")

            # Display the frame with detected faces (for debugging purposes)
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

        return JsonResponse({
            'status': 'success',
            'message': 'Face captured and saved.',
            'class_name': student.class_name,
            'division': student.division,
            'roll_no': student.roll_no,
            'name': student.name,
            'image_path': student.image.url if student.image else 'Image not saved'
        })
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def student_form_for_attendance(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the student data to the database
            student = form.save(commit=False)
            
            # Proceed to verify the face after form submission
            return check_attendance(request, student)
    else:
        form = StudentForm()

    return render(request, 'students_form.html', {'form': form})

@csrf_exempt
def check_attendance(request,student):
    if request.method == 'POST':
        # Retrieve the roll number or student ID from the request (assumed POST data)
        try:
            student = StudentImage.objects.get(roll_no=student.roll_no)
        except StudentImage.DoesNotExist:
            return JsonResponse({'error': 'Student not found.'}, status=404)

        # Open a connection to the webcam
        video_capture = cv2.VideoCapture(0)

        if not video_capture.isOpened():
            return JsonResponse({'error': 'Could not open video.'}, status=500)

        ret, frame = video_capture.read()
        if not ret:
            video_capture.release()
            return JsonResponse({'error': 'Could not read frame.'}, status=500)

        # Convert the frame to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Path to the student's saved image
        student_image_path = os.path.join(settings.MEDIA_ROOT, student.image.name)

        try:
            # Verify the face using DeepFace
            verification = DeepFace.verify(img1_path=rgb_frame, img2_path=student_image_path, detector_backend='opencv')

            if verification['verified']:
                return JsonResponse({
                    'status': 'success',
                    'message': f'Attendance marked for {student.name}.',
                    'roll_no': student.roll_no
                })
            else:
                return JsonResponse({'status': 'failed', 'message': 'Face does not match.'}, status=403)

        except Exception as e:
            print(f"Error during face verification: {e}")
            return JsonResponse({'error': 'Face verification failed.'}, status=500)

        finally:
            # Release the webcam
            video_capture.release()
            cv2.destroyAllWindows()

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
