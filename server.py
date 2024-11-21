from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from geopy.geocoders import Nominatim

app = Flask(__name__)

# SQLite database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scans.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class ScanData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Helper function to get location
def get_location():
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = request.remote_addr  # Replace with actual location fetching logic if possible
    try:
        location = geolocator.geocode(location)
        return location.address if location else "Unknown Location"
    except Exception:
        return "Location Unavailable"

@app.route('/scan', methods=['GET'])
def scan_qr():
    # Get current timestamp and location
    timestamp = datetime.utcnow()
    location = get_location()

    # Save to database
    scan_data = ScanData(location=location, timestamp=timestamp)
    db.session.add(scan_data)
    db.session.commit()

    return jsonify({
        "message": "Scan data recorded successfully!",
        "location": location,
        "timestamp": timestamp.isoformat()
    })

if __name__ == "__main__":
    # Ensure the application context is set up before creating the database
    with app.app_context():
        db.create_all()  # Create all tables in the database
        print("Database tables created successfully.")
    app.run(debug=True)

