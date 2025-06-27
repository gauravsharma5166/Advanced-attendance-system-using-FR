# Advanced Attendance System


A modern face recognition-based attendance management system for educational institutions. This project is ideal for college projects and demonstrates role-based access, intuitive management, and accurate identification using multiple images.

---

## Project Screenshots
Below are screenshots of the main features and pages of the project:

### Landing Page
![{8645BB6B-647D-481A-A776-D40C37F19D4B}](https://github.com/user-attachments/assets/a55681b2-9d7f-46e6-ab7e-d9a33ec7fceb)

The welcoming landing page introduces the system and its features.

### Login Page
![{0A64C946-6187-45C0-8D6E-96C0637FEAE8}](https://github.com/user-attachments/assets/1e7f7d26-06cb-4177-b31f-e196c7629cd1)

Secure login for administrators and lecturers.

### Dashboard Page
![image](https://github.com/user-attachments/assets/e033a187-9031-460a-b1c8-c21a4b8c5048)

Overview of attendance statistics and quick access to management features.

### Profile Page
![{CCDE5E75-4096-4AAC-AFE9-8C7584B182F8}](https://github.com/user-attachments/assets/64f4b717-3f8a-471d-a35a-d75d20fb91da)

User profile management for updating personal details and password.

### Create Class Page
![{761C56F8-5160-4427-8C19-005FCE71974E}](https://github.com/user-attachments/assets/cda34807-3ce0-4400-908d-b37ba6bda337)

Interface for administrators to create and manage classes.

### Register Student Page
![{E5F23482-0FCE-4E0F-97E6-F6CF25DE8A69}](https://github.com/user-attachments/assets/f738c29f-2bf1-4765-b9b5-d75c89f47e8b)

Add new students and capture multiple images for face recognition.

### View Students Page
![{AA3C0CC6-0007-4B9F-BAA0-1EB5F4CA6C91}](https://github.com/user-attachments/assets/ea7610d8-4c11-484d-a82c-b7ec8833f8e6)

List and manage all registered students in the system.

### Manual Attendance Page
![{FD3D633D-CB85-4FE2-9DFF-E5A3982D2F83}](https://github.com/user-attachments/assets/abf3756d-f7e4-4714-856a-fa106b4deadc)

Mark attendance manually for students in a class.

### Image-based Attendance Page
![image](https://github.com/user-attachments/assets/a778edac-dbbf-44d2-986b-fc1ee6d509fb)

Mark attendance by uploading or capturing student images.

### Webcam Attendance Page
![image](https://github.com/user-attachments/assets/911e600f-dcb8-47e4-8c9c-8da6d22cbd20)


Take attendance using live webcam face recognition.

### View Attendance Page
![{BDCF4D00-9EFD-40B5-8BE6-139A0BDE2AA5}](https://github.com/user-attachments/assets/92fc56a9-4f90-4a70-9e19-4124eaad58bd)

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
