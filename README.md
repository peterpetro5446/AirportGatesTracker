# ParkingTrack

A smart parking lot monitoring system that detects planes, tracks their positions, and manages parking gates using computer vision and bounding box data.

## Project Features

- Vehicle detection and tracking
- JSON-based bounding box input
- Web-based frontend interface
- Parking space management logic

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

# 3. Run Api
python app.py