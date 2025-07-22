import os
import json
from firebase_admin import credentials, initialize_app, db


firebase_cred_json = os.environ.get("FIREBASE_CREDENTIALS")

if not firebase_cred_json:
    raise ValueError("Missing FIREBASE_CREDENTIALS environment variable")


cred_dict = json.loads(firebase_cred_json)
cred = credentials.Certificate(cred_dict)


firebase_app = initialize_app(cred, {
    'databaseURL': 'https://smartserve-17598-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

def get_db():
    return db.reference("/")
