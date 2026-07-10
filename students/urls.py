from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('departments/', views.department, name='department'),

    path('student/add/', views.student_form, name='student_form'),
    path('student/create/', views.student_post, name='student_post'),

    path('student/edit/<int:pk>/', views.student_edit, name='student_edit'),
    path('student/delete/<int:pk>/', views.student_delete, name='student_delete'),
]