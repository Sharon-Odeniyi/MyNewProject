# MyNewProject

A web-based **Student Management System** built with **Django** for managing student records in a simple and organized way. The application provides a central interface where student details can be stored, viewed, updated, and removed.

## Overview

**MyNewProject** is a Django student management application designed to handle basic student record operations. The system displays student records on the homepage in a tabular format and allows users to edit or delete records directly from that page. It also includes a separate form for adding new students and a departments page as part of the application structure.

The project currently supports the core CRUD workflow for student data and serves as a practical implementation of Django models, views, templates, forms, and URL routing.

## Features

- Display all student records on the homepage in a table
- Add new student records through a form
- Edit student details directly from the homepage
- Delete student records directly from the homepage
- Departments page
- Django admin panel access
- Superuser authentication for administrative control

## Student Data Fields

Each student record contains the following information:

- **Name**
- **Matric Number**
- **Email**
- **Level**
- **Department**

## Tech Stack

- **Python**
- **Django**
- **HTML**
- **CSS**
- **SQLite**

## How the Application Works

### Homepage
The homepage functions as the main dashboard of the application. It displays all student records in a table and provides quick access to student management actions.

From the homepage, a user can:
- View all student records
- Edit a student record
- Delete a student record

### Add Student Page
The application includes a form for adding new students into the system. Submitted records are stored in the database and reflected on the homepage table.

### Departments Page
A departments page is included as part of the application structure.

### Admin Panel
The system also uses Django’s built-in admin panel, allowing a superuser to manage student data through the backend.

## Project Structure

```text
MyNewProject/
│
├── manage.py
├── MyNewProject/
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

## Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the repository

```powershell
git clone https://github.com/Sharon-Odeniyi/MyNewProject.git
cd MyNewProject
```

### 2. Create a virtual environment

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

**PowerShell**
```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Django

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

### 7. Run the development server

```powershell
python manage.py runserver
```

### 8. Open the project in your browser

- **Home page:** `http://127.0.0.1:8000/`
- **Admin panel:** `http://127.0.0.1:8000/admin/`

## Admin Access

The project uses Django’s built-in admin system. After creating a superuser, you can log into the admin dashboard and manage student records directly.

```powershell
python manage.py createsuperuser
```

Then visit:

`http://127.0.0.1:8000/admin/`

## Current Status

The following parts of the project have been implemented:

- Django project setup
- `students` app creation
- Student model with the fields:
  - `name`
  - `matricno`
  - `email`
  - `level`
  - `department`
- Homepage displaying all student records in a table
- Add student form
- Edit student functionality
- Delete student functionality
- Departments page
- Superuser/admin configuration

## Possible Improvements

This project can be extended with additional features such as:

- Search students by name or matric number
- Filter students by department or level
- Student detail/profile page
- Pagination for large student records
- Authentication and role-based access
- Improved UI styling with Bootstrap
- Attendance management
- Result/grade management
- Dashboard analytics for student data

## Learning Objectives

This project demonstrates practical use of core Django concepts, including:

- Project and app structure in Django
- Model creation and database design
- Form handling and validation
- CRUD operations
- Views and URL routing
- Template rendering
- Django admin configuration
- Database migrations

## Conclusion

**MyNewProject** is a simple but functional Django-based Student Management System that supports the core operations needed to manage student records. With the homepage serving as the central dashboard for viewing, editing, and deleting student data, the project provides a solid foundation for building a more advanced academic management platform.

## Author

**Sharon Odeniyi**
