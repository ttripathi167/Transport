from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import bson


client = MongoClient("mongodb://localhost:27017/")  
db = client['MYDB1'] 


users = db['users']
vehicles = db['vehicles']
schedules = db['schedules']
bookings = db['bookings']



def register_user(name, email, password, role='user'):
    if users.find_one({"email": email}):
        return "Email already exists."
    hashed_password = generate_password_hash(password)
    users.insert_one({"name": name, "email": email, "password": hashed_password, "role": role})
    return "Registration successful!"

def login_user(email, password):
    user = users.find_one({"email": email})
    if user and check_password_hash(user['password'], password):
        return user
    return None

def add_vehicle(vehicle_type, capacity, status):
    vehicles.insert_one({"type": vehicle_type, "capacity": capacity, "status": status})
    return "Vehicle added successfully."

def add_schedule(route, departure_time, arrival_time, vehicle_id):
    schedules.insert_one({
        "route": route,
        "departure_time": departure_time,
        "arrival_time": arrival_time,
        "vehicle_id": vehicle_id
    })
    return "Schedule added successfully."

def book_schedule(user_id, schedule_id):
    booking_date = datetime.now().strftime('%Y-%m-%d')
    bookings.insert_one({
        "user_id": user_id,
        "schedule_id": bson.ObjectId(schedule_id),
        "booking_date": booking_date,
        "status": "confirmed"
    })
    return "Booking confirmed."
