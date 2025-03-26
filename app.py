from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

parking_data = {
    "total_spots": 24,
    "occupied": 0,
    "available": 24,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

@app.route("/api/parking-status", methods=["GET"])
def get_parking_status():
    parking_data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Update timestamp
    return jsonify(parking_data)

# ✅ FIX: Add `update-parking` route
@app.route("/api/update-parking", methods=["POST"])
def update_parking():
    data = request.json
    if not data:
        return jsonify({"error": "No data received"}), 400  # Handle empty requests
    if "occupied" in data and "available" in data:
        parking_data["occupied"] = data["occupied"]
        parking_data["available"] = data["available"]
        parking_data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return jsonify({"message": "Parking data updated successfully"}), 200
    return jsonify({"error": "Invalid data format"}), 400  # Handle missing fields

if __name__ == "__main__":
    app.run(debug=True)
