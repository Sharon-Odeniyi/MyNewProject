from django import views
from django.urls import path
from students import views
from .views import home, department, student_post, student_form, student_edit, student_delete


urlpatterns = [
    path('', views.home, name='home'),
    path('departments/', views.department, name='department'),
    path('student_post/', views.student_post, name='student_post'),
    path('student_form/', views.student_form, name='student_form'),
    
    path('student/edit/<int:pk>/', views.student_edit, name='student_edit'),
    path('student/delete/<int:pk>/', views.student_delete, name='student_delete'),
]