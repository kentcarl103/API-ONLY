from flask import jsonify, request
from app.firebase import get_db
from app.models.User import User  

# USERS
def login_user(data):
    email = data.get("email")
    password = data.get("password")

    users = get_db().child("users").get()

    if not users:
        return jsonify({"error": "No users found"}), 404

    
    for user_id, user in users.items():
        if user.get("email", "").lower() == email.lower():
            if user.get("password") == password:
                return jsonify({
                    "message": "Login successful",
                    "user": {
                        "id": user_id,
                        "email": user.get("email"),
                        "name": user.get("name", "User")
                    }
                }), 200
            else:
                return jsonify({"error": "Invalid password"}), 401

    return jsonify({"error": "User not found"}), 404

def signup_user(data):
    email = data.get("email")
    password = data.get("password")
    firstname = data.get("firstname")
    lastname = data.get("lastname")
    middlename = data.get("middlename", "")
    position = data.get("position")

    if not email or not password or not firstname or not lastname or not position:
        return jsonify({"error": "Missing required fields"}), 400

    users_ref = get_db().child("users")
    existing_users = users_ref.get()

    if existing_users:
        for user in existing_users.values():
            if user.get("email", "").lower() == email.lower():
                return jsonify({"error": "User already exists"}), 409

    user_obj = User(
        firstname=firstname,
        middlename=middlename,
        lastname=lastname,
        email=email,
        password=password,
        position=position
    )

    result = users_ref.push(user_obj.to_dict())

    full_name = f"{firstname} {middlename} {lastname}".strip()

    return jsonify({
        "message": "Signup successful",
        "user": {
            "id": result.key,
            "email": email,
            "name": full_name,
            "position": position
        }
    }), 201


def get_all_users():
    users = get_db().child("users").get()

    if not users:
        return jsonify({"users": []}), 200

    clean_users = [
        {
            "id": uid,
            "email": user.get("email"),
            "name": f"{user.get('firstname', '')} {user.get('middlename', '')} {user.get('lastname', '')}".strip(),
            "position": user.get("position", "")
        }
        for uid, user in users.items()
    ]

    return jsonify({
        "message": "All users fetched successfully",
        "users": clean_users
    }), 200


def get_user_by_id(user_id):
    user = get_db().child("users").child(user_id).get()

    if not user:
        return jsonify({"error": "User not found"}), 404

    full_name = f"{user.get('firstname', '')} {user.get('middlename', '')} {user.get('lastname', '')}".strip()

    return jsonify({
        "user": {
            "id": user_id,
            "email": user.get("email"),
            "name": full_name,
            "position": user.get("position", "")
        }
    }), 200


def get_user_by_email(email):
    users = get_db().child("users").get()

    if not users:
        return jsonify({"error": "User not found"}), 404

    for uid, user in users.items():
        if user.get("email", "").lower() == email.lower():
            full_name = f"{user.get('firstname', '')} {user.get('middlename', '')} {user.get('lastname', '')}".strip()
            return jsonify({
                "user": {
                    "id": uid,
                    "email": user["email"],
                    "name": full_name,
                    "position": user.get("position", "")
                }
            }), 200

    return jsonify({"error": "User not found"}), 404


# RESTAURANT OWNERS
def owner_login(data):
    email = data.get("email")
    password = data.get("password")

    owners = get_db().child("owners").get()

    if not owners:
        return jsonify({"error": "No owners found"}), 404

    for owner_id, owner in owners.items():
        if owner.get("email", "").lower() == email.lower():
            if owner.get("password") == password:
                return jsonify({
                    "message": "Owner login successful",
                    "owner": {
                        "id": owner_id,
                        "email": owner["email"],
                        "name": owner.get("name", "")
                    }
                }), 200
            return jsonify({"error": "Invalid password"}), 401

    return jsonify({"error": "Owner not found"}), 404


def get_all_owners():
    owners = get_db().child("owners").get()

    if not owners:
        return jsonify({"owners": []}), 200

    clean_owners = [
        {
            "id": oid,
            "email": owner.get("email"),
            "name": owner.get("name", "")
        }
        for oid, owner in owners.items()
    ]

    return jsonify({
        "owners": clean_owners
    }), 200
