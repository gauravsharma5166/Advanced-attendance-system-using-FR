# Advanced Attendance System

## Overview
The Advanced Attendance System is a modern face recognition-based attendance management system designed to simplify and enhance attendance tracking for educational institutions. It leverages Flask for the backend, MongoDB for data storage, and face recognition technology for identifying students.

## Features
- **Face Recognition Attendance**: Mark attendance using face recognition technology.
- **Manual Attendance**: Option to mark attendance manually.
- **Live Webcam Attendance**: Real-time attendance marking using a webcam.
- **Student Management**: Add, view, and delete students.
- **Class Management**: Manage classes and their associated students.
- **Attendance Reports**: View detailed attendance records and export them to Excel.
- **Dark Mode**: Toggle between light and dark themes.

## Project Structure
```
├── app.py                 # Main Flask application
├── database.py            # MongoDB connection logic
├── encode_faces.py        # Face encoding logic
├── init_db.py             # Database initialization
├── migrate_data.py        # Data migration script
├── test_mongo_connection.py # MongoDB connection testing
├── requirements.txt       # Project dependencies
├── Procfile               # Deployment configuration for Heroku
├── gunicorn.conf.py       # Gunicorn configuration
├── static/                # Static files
│   ├── attendance_sheets/ # Excel attendance sheets
│   ├── class_photos/      # Class photos
│   ├── img/               # Icons and images
│   └── student_photos/    # Student photos
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   ├── landing.html       # Landing page
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   ├── dashboard.html     # Dashboard
│   ├── view_students.html # View students
│   ├── view_attendance.html # View attendance
│   ├── mark_attendance_image.html # Mark attendance using images
│   ├── mark_attendance_manual.html # Mark attendance manually
│   ├── live_attendance.html # Live webcam attendance
│   └── manage_classes.html # Manage classes
└── README.md              # Project documentation
```

## Installation

### Prerequisites
- Python 3.8 or higher
- MongoDB (local or Atlas)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Advanced-Attendance-System
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following:
     ```env
     MONGO_URI=<your-mongodb-uri>
     ```
5. Initialize the database:
   ```bash
   python init_db.py
   ```
6. Run the application:
   ```bash
   python app.py
   ```

## Deployment
The project is configured for deployment on Heroku. Use the `Procfile` and `gunicorn.conf.py` for deployment.

## License
This project is licensed under the MIT License.

## Contributors
- Your Name
- Additional Contributors

## Acknowledgments
- Flask
- MongoDB
- Face Recognition Library
- Bootstrap
- Font Awesome

---
