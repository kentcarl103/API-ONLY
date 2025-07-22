from app.firebase import get_db
from flask import jsonify, request
from datetime import datetime

def update_detection():
    try:
        data = request.get_json()

        vacant_chairs = data.get("vacant_chairs")
        vacant_tables = data.get("vacant_tables")

        if vacant_chairs is None or vacant_tables is None:
            return jsonify({"error": "Missing fields in data"}), 400

        detection_data = {
            "vacant_chairs": vacant_chairs,
            "vacant_tables": vacant_tables,
            "timestamp": datetime.utcnow().isoformat()
        }

        db_ref = get_db()

        # Save to historical list
        db_ref.child("detections").push(detection_data)

        # Save to latest (singular path)
        db_ref.child("detection").child("latest").set(detection_data)

        return jsonify({"message": "Detection data updated successfully."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_latest_detection():
    try:
        db_ref = get_db()
        data = db_ref.child("detection").child("latest").get()

        if not data:
            return jsonify({"error": "No detection data found"}), 404

        return jsonify(data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500