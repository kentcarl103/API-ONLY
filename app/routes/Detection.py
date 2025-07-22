from flask import Blueprint
from app.controllers.DetectionController import update_detection,get_latest_detection

detection_bp = Blueprint('detection_bp', __name__)

@detection_bp.route('/update', methods=['POST'])
def update_detection_route():
    return update_detection()

@detection_bp.route('/latest', methods=['GET'])
def get_latest_detection_route():
    return get_latest_detection()
