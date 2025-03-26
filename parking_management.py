import cv2
import json
from ultralytics import solutions
import requests

# Video capture
cap = cv2.VideoCapture("resources/videoSource.mp4")
assert cap.isOpened(), "Error reading video file"

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("resources/parking_management.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

#  Initialize parking management with tracking
parkingmanager = solutions.ParkingManagement(
    model="models/yolo11x.pt",  # path to model file
    json_file="bounding_boxes.json",  # path to parking annotations file
    tracker="botsort.yaml" # botsort for better accuracy but slower detection
) 

# Set confidence and IoU thresholds
parkingmanager.model.conf = 0.15  # Lower threshold for small object detection
parkingmanager.model.iou = 0.15   # Looser IoU for overlapping objects

while cap.isOpened():
    ret, im0 = cap.read()
    if not ret:
        break

    results = parkingmanager(im0)  # `results` is a `SolutionResults` object

    #  Get occupied and available spots directly from SolutionResults
    occupied = results.filled_slots  # Occupied parking spots
    available = results.available_slots  # Available parking spots

    # Send updated parking status to Flask
    parking_status = {
        "occupied": occupied,
        "available": available
    }
    
    # 🛠 Send POST request & handle errors
    try:
        response = requests.post("http://127.0.0.1:5000/api/update-parking", json=parking_status)
        if response.status_code == 200:
            print("API Response:", response.json())  # Print response from server
        else:
            print("API Error:", response.status_code, response.text)  # Print raw error
    except requests.exceptions.RequestException as e:
        print("Request Failed:", e)

    video_writer.write(results.plot_im)  # Save processed frame
    cv2.imshow("Parking Management", results.plot_im)  # Show output

    # Optional: Press 'q' to quit early
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
video_writer.release()
cv2.destroyAllWindows()
print("Video processing complete")
