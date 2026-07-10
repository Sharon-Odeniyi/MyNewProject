from django.contrib import admin

from students.models import Department, Student


# Register your models here.
admin.site.register(Department)
admin.site.register(Student)