from firebase_admin import credentials, initialize_app, db

cred = credentials.Certificate("C:/Users/kentc/OneDrive/Desktop/SMARTSERVE/SampleAPI/firebase_credentials.json")
firebase_app = initialize_app(cred, {
    'databaseURL': 'https://smartserve-17598-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

def get_db():
    return db.reference("/")
