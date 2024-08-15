# Privacy-Protector

**Project Name:** Face Detection for Automatic Screen Lock

**Description:**

This Python script utilizes OpenCV (cv2) and MediaPipe (mp) to detect faces in a webcam feed and automatically lock the screen after a specified period of inactivity.

**Features:**

- Leverages MediaPipe's efficient face detection model.
- Configurable lock delay for personalization.
- Displays real-time webcam feed with bounding boxes around detected faces (optional).

**Installation:**

1. Ensure you have Python (>=3.6) installed.
2. Install required libraries using pip:

   ```bash
   pip install opencv-python mediapipe
   ```

**Usage:**

1. Clone or download the repository.
2. Run the script from your terminal:

   ```bash
   python face_detection_screen_lock.py
   ```

**Configuration:**

- Modify the `lock_delay` variable in the `main` function to adjust the time (in seconds) before locking after no face is detected.

**Code Documentation:**

**Imports:**

- `cv2`: OpenCV library for computer vision tasks like video capture and image processing.
- `mediapipe`: Machine learning framework providing face detection functionality.
- `os`: Python's operating system module for interacting with the system (used for screen locking).
- `time`: Python's time module for time-related operations (used for face detection delays).
- `sys`: Python's system module for handling system exits (used for error handling).

**`main` Function:**

1. **Initialization:**
   - Initializes MediaPipe's face detection model with a minimum detection confidence threshold (default: 0.2).
   - Creates a drawing utility object from MediaPipe for visualization (optional).
   - Captures video from the default webcam using OpenCV's video capture.
   - Sets `face_detected` to `True` initially, assuming a face is present at the start.
   - Initializes `last_detection_time` to the current time and configures the `lock_delay` (screen lock time after no face detection).

2. **Main Loop:**
   - Continuously reads frames from the video capture.
   - Exits the loop gracefully if frame reading fails.
   - Converts the frame to RGB format (required for MediaPipe face detection).
   - Processes the frame using the face detection model to get detection results.
   - Updates the current time.

   - **Face Detected:**
     - If results contain detections (face found):
       - If `face_detected` was previously `False` (face wasn't detected), set it back to `True` and update `last_detection_time` to the current time.
       - Prints a message indicating face detection and screen unlocking.
       - Optionally draws bounding boxes around detected faces.

   - **No Face Detected:**
     - If `face_detected` was previously `True` and the current time minus `last_detection_time` exceeds `lock_delay`:
       - Sets `face_detected` to `False`.
       - Locks the screen using `os.system('rundll32.exe user32.dll,LockWorkStation')`.
       - Prints a message indicating no face detection and screen locking.
       - Updates `last_detection_time` to the current time.

   - **Display Camera Feed (Optional):**
     - Displays the webcam feed with bounding boxes around detected faces (if enabled) using OpenCV's `imshow` function.

3. **Keyboard Input:**
   - Waits for a key press.
   - Exits the loop and releases resources if the 'q' key is pressed.

4. **Resource Cleanup:**
   - Releases the video capture object.
   - Destroys all OpenCV windows.

5. **Error Handling:**
   - Catches any exceptions (`Exception`) that might occur during execution.
   - Prints an error message with details.
   - Exits the program with a non-zero status code (1) to indicate an error.

**Additional Considerations:**

- For more advanced screen locking logic (e.g., password prompts), explore system-specific APIs or libraries.
- Consider implementing a timeout mechanism for the webcam feed to conserve resources.
- You can incorporate settings for different detection confidence thresholds or enabling/disabling the visualization.
