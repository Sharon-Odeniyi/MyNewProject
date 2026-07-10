# MyNewProject
# Student Management System

A web-based **Student Management System** built with **Django** for managing student records efficiently.  
This project provides a simple interface for administrators to add, update, and delete student information, while also making use of Django’s built-in admin system for backend management.

## Overview

The Student Management System is designed to simplify the process of storing and managing student records in one place. It currently supports the core CRUD operations required for basic student administration:

- **Create** student records  
- **Update** student information  
- **Delete** student records  

The project also includes a homepage and a configured Django superuser account for administrative access.

## Features

- Homepage for the application
- Add new student records
- Edit student details
- Delete student records
- Django admin panel integration
- Superuser authentication for admin access
- Structured foundation for future expansion

## Built With

- **Python**
- **Django**
- **HTML**
- **CSS**
- **SQLite**

## Current Project Status

The following parts of the system have been completed:

- Django project setup and configuration
- Superuser creation for admin access
- Homepage design and implementation
- Student add functionality
- Student edit functionality
- Student delete functionality

## How the System Works

The system is built to allow an administrator manage student information from a central web interface.

At the moment, the application allows the admin to:

1. Access the homepage of the application
2. Add a new student into the system
3. Edit existing student information
4. Delete student records when necessary
5. Manage additional data through the Django admin dashboard

This makes it a simple but functional student record management application that can be extended into a full school management platform.

## Installation Guide

Follow the steps below to run the project locally on your machine.

### 1. Clone the repository
``` powershell
git clone https://github.com/your-username/student-management-system.git
cd student-management-system
```

### 2. Create a virtual environment

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

**Windows**
```powershell
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```powershell
pip install django
```

### 5. Apply migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser

```powershell
python manage.py createsuperuser
```

Follow the prompts to set up your admin username and password.

### 7. Run the development server

```powershell
python manage.py runserver
```

### 8. Open the project in your browser

```powershell
http://127.0.0.1:8000/
```

---

## Admin Dashboard

To access the Django admin panel, go to:

```powershell
http://127.0.0.1:8000/admin/
```

Log in using the superuser credentials created with:

```powershell
python manage.py createsuperuser
```

---

## Project Structure

A typical structure of the project may look like this:

student_management_system/
│
├── manage.py
├── student_management_system/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── forms.py
```

---
