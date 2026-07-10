from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student, Department
from .form import StudentForm   # ✅ FIXED IMPORT
from datetime import datetime


# =========================
# LEVEL CALCULATION (ONE SOURCE OF TRUTH)
# =========================
def calculate_level(matric_no):
    try:
        current_year = datetime.now().year
        admission_year = 2000 + int(matric_no[:2])

        year_diff = current_year - admission_year + 1

        level_map = {
            1: "100 Level",
            2: "200 Level",
            3: "300 Level",
            4: "400 Level",
            5: "500 Level",
        }

        return level_map.get(year_diff, "Graduated")
    except:
        return "Unknown"


# =========================
# HOME
# =========================
def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})


# =========================
# DEPARTMENT
# =========================
def department(request):
    departments = Department.objects.all()
    return render(request, 'department.html', {'departments': departments})


# =========================
# SHOW FORM
# =========================
def student_form(request):
    departments = Department.objects.all()
    return render(request, 'student_form.html', {'departments': departments})


# =========================
# CREATE STUDENT
# =========================
def student_post(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            student = form.save(commit=False)


            student.save()
            messages.success(request, "Student added successfully.")
            return redirect("home")

        messages.error(request, "Invalid form data.")

    return redirect("student_form")


# =========================
# EDIT STUDENT
# =========================
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.firstname = request.POST.get('firstname')
        student.lastname = request.POST.get('lastname')
        student.matric_no = request.POST.get('matric_no')
        student.email = request.POST.get('email')
        student.level = calculate_level(student.matric_no)

        department_id = request.POST.get('department')

        try:
            student.department = Department.objects.get(id=department_id)
        except Department.DoesNotExist:
            student.department = None

       

        student.save()
        return redirect('home')

    departments = Department.objects.all()
    return render(request, 'edit_student.html', {
        'student': student,
        'departments': departments
    })


# =========================
# DELETE STUDENT
# =========================
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('home')