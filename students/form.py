from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["firstname", "lastname", "matric_no", "email", "department"]
        widgets = {
            "firstname": forms.TextInput(attrs=
                {"class": "form-control",
                 "placeholder": "Enter First Name"
                 }),
            "lastname": forms.TextInput(attrs=
                {"class": "form-control", 
                 "placeholder": "Enter Last Name"
                 }),
            "matric_no": forms.TextInput(attrs=
                {"class": "form-control", 
                 "placeholder": "Enter Matric Number"
                 }),
            "email": forms.EmailInput(attrs=
                {"class": "form-control", 
                 "placeholder": "Enter Email"
                 }),
            "department": forms.Select(attrs=
                {"class": "form-control", 
                 "placeholder": "Select Department"
                 }),
        }