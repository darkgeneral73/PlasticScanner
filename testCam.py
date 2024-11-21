import cv2
cap = cv2.VideoCapture(0)  # Try 0 or 1 for different cameras
if not cap.isOpened():
    print("Error: Unable to access the camera.")
else:
    print("Camera is working!")
    cap.release()

