# Advanced Attendance System

## View Live Demo

A modern face recognition-based attendance management system for educational institutions. This project is ideal for college projects and demonstrates role-based access, intuitive management, and accurate identification using multiple images.

---

## Project Screenshots
Below are screenshots of the main features and pages of the project:

### Landing Page
The welcoming landing page introduces the system and its features.

### Login Page
Secure login for administrators and lecturers.

### Dashboard Page
Overview of attendance statistics and quick access to management features.

### Profile Page
User profile management for updating personal details and password.

### Create Class Page
Interface for administrators to create and manage classes.

### Register Student Page
Add new students and capture multiple images for face recognition.

### View Students Page
List and manage all registered students in the system.

### Manual Attendance Page
Mark attendance manually for students in a class.

### Image-based Attendance Page
Mark attendance by uploading or capturing student images.

### Webcam Attendance Page
Take attendance using live webcam face recognition.

### View Attendance Page
View and export attendance records for analysis.

---

## Features
- Role-based access for administrators and lecturers.
- Manage classes, add students, view attendance records through an intuitive interface.
- Capture and store multiple images for accurate identification.
- Export attendance records to Excel.
- User-friendly dashboard for both admin and lecturer roles.
- Great for college projects and demonstrations.

---

## Project Structure
```
├── app.py
├── database.py
├── encode_faces.py
├── init_db.py
├── migrate_data.py
├── requirements.txt
├── static/
│   ├── attendance_sheets/
│   ├── class_photos/
│   ├── img/
│   └── student_photos/
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── landing.html
│   └── ...
└── ...
```

---

## Setup Procedure
Follow these steps to set up and run the project:

### Clone or Download the Repository
```bash
git clone https://github.com/gauravsharma5166/Advanced-attendance-system-using-FR
```

### Set Up the Database
Run the database initialization script:
```bash
python init_db.py
```

### Launch the Application
Start the Flask app:
```bash
python app.py
```

Visit the application in your browser:
```
http://localhost/{your-project-folder-name}
```

---

## User Guide

### 1. Login as Administrator
- **Email:** admin
- **Password:** admin123

Once logged in, you can:
- Add students
- Manage classes.

⚠️ **Important:**
- Ensure to add at least two students.
- Poor image quality will affect recognition accuracy. You can retake any image by clicking on it.

### 2. Login as Lecturer
- Create a lecturer account via the admin panel or use a pre-existing one.
- Select lecture user type to be able to login as lecturer.

- **Email:** admin
- **Password:** admin123

As a lecturer:
- Select a course on the home page.
- Launch the Face Recognition feature to begin attendance.

### Additional Features for the Lecturer Panel
- Export the attendance to an Excel sheet.
- Other simple features are available for managing the lecture panel.

---

For any issues or contributions, please open an issue or pull request on the GitHub repository.
