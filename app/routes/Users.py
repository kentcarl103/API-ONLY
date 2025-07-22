from flask import Blueprint, request
from app.controllers.UserController import (
    login_user, signup_user, get_all_users, get_user_by_id,
    get_user_by_email, owner_login, get_all_owners
)

users_bp = Blueprint('users_bp', __name__)

@users_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return login_user(data)

@users_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    # Optional fields check for safe defaults
    data.setdefault('middlename', '')

    required_fields = ['firstname', 'lastname', 'email', 'password', 'position']
    missing_fields = [field for field in required_fields if not data.get(field)]

    if missing_fields:  
        return {"error": f"Missing required fields: {', '.join(missing_fields)}"}, 400

    return signup_user(data)

@users_bp.route('/', methods=['GET'])
def get_users():
    return get_all_users()

@users_bp.route('/id', methods=['GET'])
def get_user_by_id_route():
    user_id = request.args.get('id')
    if not user_id:
        return {"error": "ID query parameter is required."}, 400
    return get_user_by_id(user_id)

@users_bp.route('/email', methods=['GET'])
def get_user_by_email_route():
    email = request.args.get('email')
    if not email:
        return {"error": "Email query parameter is required."}, 400
    return get_user_by_email(email)

@users_bp.route('/owner/login', methods=['POST'])
def owner_login_route():
    data = request.get_json()
    return owner_login(data)

@users_bp.route('/users/owner', methods=['GET'])
def get_all_owners_route():
    return get_all_owners()
