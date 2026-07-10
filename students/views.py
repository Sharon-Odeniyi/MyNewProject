from urllib import request

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
# ADD STUDENT FORM
# =========================
def student_form(request):
    form = StudentForm()
    return render(request, 'student_form.html', {'form': form})


# =========================
# CREATE STUDENT
# =========================
def student_post(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully.")
            return redirect("home")


        else:
            messages.error(request, "Invalid form data.")

    return redirect("student_form")


# =========================
# EDIT STUDENT
# =========================
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully.")
            return redirect("home")
        else:
            messages.error(request, "Invalid form data.")
    else:
        form = StudentForm(instance=student)

    return render(request, "edit_student.html", {
        "form": form,
          "student": student
          })




# =========================
# DELETE STUDENT
# =========================
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully.")
        return redirect('home')

    return render(request, 'delete_student.html', {'student': student})