# Transport Management System

## Overview
The **Transport Management System (TMS)** is a web application built using Streamlit, MongoDB, and Python to manage transport operations. The system allows users to register, log in, add vehicles, schedule routes, and book schedules. It provides both user and admin functionalities for easy transport management.

## Features
- **User Registration and Login**: Users can register and log in to access various features.
- **Admin Features**: Admins can add new vehicles and schedules.
- **Schedule Booking**: Users can book available schedules.
- **MongoDB Integration**: Data is stored and retrieved from MongoDB for user, vehicle, schedule, and booking information.

## Requirements
- Python 3.x
- Streamlit
- MongoDB
- Werkzeug
- Pymongo

## Usage

### 1. Register
Users can create an account by entering their name, email, password, and role (user/admin).

### 2. Login
Registered users can log in using their email and password.

### 3. Admin Features
Admins can add vehicles and schedules for users to book.
  - **Add Vehicle**: Enter the vehicle type, capacity, and status.
  - **Add Schedule**: Enter the route, departure/arrival times, and select a vehicle.

### 4. Book Schedule
Logged-in users can book available schedules from the system.

### 5. Logout
Users can log out of the system, which will end their session.

## Technologies Used
- **Streamlit**: For building the web application interface.
- **MongoDB**: For storing user, vehicle, schedule, and booking data.
- **Werkzeug**: For password hashing (secure login).
- **Python**: For backend logic and database interaction.

## Future Enhancements
- Add email verification during registration.
- Implement user-specific booking history.
- Integrate payment gateway for booking payments.
- Add more features such as tracking vehicles in real-time.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **Streamlit**: For creating an easy-to-use framework for building interactive web applications.
- **MongoDB**: For providing an efficient NoSQL database solution.
- **Werkzeug**: For simplifying password management.
