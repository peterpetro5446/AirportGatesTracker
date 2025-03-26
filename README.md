# ParkingTrack

A smart parking lot monitoring system that detects planes, tracks their positions, and manages parking gates using computer vision and bounding box data. With the usage of Flask API occupancy data is extracted into a HTML.

## Project Features

- Video footage recorded from Microsoft Flight Simulator 2024
- Vehicle detection and tracking
- JSON-based bounding box input
- Web-based frontend interface
- Parking space management logic applied to Orlando International Airport - Terminal A - Gates 1 - 29

## Project Structure

ParkingTrack/ 
├── models/ # Contains trained models or configurations 
├── resources/ # Static assets: images, videos, etc. 
├── venv/ # Virtual environment (excluded via .gitignore) 
│ 
├── app.py # Main entry point (e.g., Flask/FastAPI server) 
├── parking_management.py # Core logic for tracking and managing spaces 
├── bounding_boxes.json # Example input data (vehicle bounding boxes) 
├── index.html # Frontend web interface 
│ 
├── requirements.txt # Python package dependencies 
└── README.md # Project documentation

## Setup

```bash
# 1. Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3.0 <Optional> Set trained model's size / complexity to desired level / hardware limitations
Modifying model = model="models/yolo11x.pt" line replace x in yolo11x.pt
    available options in asceding order of their complexity: n < s < m < l < x
    where n = nano, s = small, m = medium, l = large, x = extra large

# 3.1 Run parking mangement file
Python parking_management.py

####  Press Q to quit Parking_management.py
####  Press Ctrl + C to quit Flask Api (app.py)

# 4. Run Api
python app.py

#5 Open index.html in a web browser
