import cv2
from pyzbar.pyzbar import decode
import requests

def scan_qr_code():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    print("Starting QR Code scanner... Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture video. Exiting...")
            break

        # Decode the QR code in the frame
        for barcode in decode(frame):
            qr_data = barcode.data.decode('utf-8')  # Extract data from QR code
            print(f"QR Code Data: {qr_data}")

            # Send the data to the server
            try:
                response = requests.get(qr_data)
                if response.status_code == 200:
                    print("Server Response:", response.json())
                else:
                    print(f"Error connecting to server: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print("Error:", e)

            # Stop scanning after the first QR code is detected
            print("QR code scanned. Exiting scanner.")
            cap.release()
            cv2.destroyAllWindows()
            return

        # Display the video feed
        cv2.imshow("QR Code Scanner", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting scanner.")
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr_code()

