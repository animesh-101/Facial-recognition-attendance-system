import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': ''   #add the URL of the database here.
})

ref = db.reference('students')

data = {
    '201061101617': {
        "name": "Animesh Raj",
        "major": "computer Science",
        "start_year": 2020,
        "total_attendance": 11,
        "standing": "Good",
        "year": 4,
        "last_attendance_time": "2023-09-24 09:00:00"
    },
    '852741': {
        "name": "Emily Blunt",
        "major": "computer Science",
        "start_year": 2020,
        "total_attendance": 21,
        "standing": "Avg",
        "year": 4,
        "last_attendance_time": "2023-09-24 09:05:00"
    },
    '963852': {
        "name": "Elon Musk",
        "major": "Physics",
        "start_year": 2020,
        "total_attendance": 7,
        "standing": "Good",
        "year": 4,
        "last_attendance_time": "2023-09-24 09:10:00"
    },
}

for key, value in data.items():
    ref.child(key).set(value)
