import cv2
import mediapipe as mp
import os
import time
import sys

def main():
    try:
        # Initialize MediaPipe Face Detection
        mp_face_detection = mp.solutions.face_detection
        face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.2)
        mp_drawing = mp.solutions.drawing_utils

        cap = cv2.VideoCapture(0)

        face_detected = True  # Assume face is detected initially
        last_detection_time = time.time()
        lock_delay = 10  # Time (in seconds) to wait before locking if no face is detected

        while True:
            ret, frame = cap.read()
            if not ret:
                break  # Exit the loop if the video capture fails

            # Convert the image to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_detection.process(rgb_frame)

            current_time = time.time()
            if results.detections:
                # Face detected
                if not face_detected:
                    face_detected = True
                    last_detection_time = current_time
                    print("Face detected, keeping screen unlocked.")
                # Draw the face detections
                for detection in results.detections:
                    bboxC = detection.location_data.relative_bounding_box
                    ih, iw, _ = frame.shape
                    bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                           int(bboxC.width * iw), int(bboxC.height * ih)
                    cv2.rectangle(frame, bbox, (0, 255, 0), 2)
            else:
                # No face detected
                if face_detected and current_time - last_detection_time > lock_delay:
                    face_detected = False
                    os.system("rundll32.exe user32.dll,LockWorkStation")
                    print("No face detected, locking screen.")
                    last_detection_time = current_time
                    

            # Display the webcam feed (optional)
            cv2.imshow('Face Detection', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
