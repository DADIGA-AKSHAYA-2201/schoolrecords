from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.getStudents, name='student_list'),
    path('add-student/', views.addStudent, name='add_student'),
    path('delete-student/<str:student_id>/', views.delete_student, name='delete_student'),
    path('update-student/<str:student_id>/', views.update_student, name='update_student'),
    path('faculties/', views.faculty_list, name='faculty_list'),
    path('faculties/add/', views.add_faculty, name='add_faculty'),
    path('faculties/update/<str:pk>/', views.update_faculty, name='update_faculty'),
    path('faculties/delete/<str:pk>/', views.delete_faculty, name='delete_faculty'),
    path('add_grade/', views.add_grade, name='add_grade'),
    path('view_grades/<str:student_id>/', views.view_grades, name='view_grades'),
    path('update_grade/<int:grade_id>/', views.update_grade, name='update_grade'),
    path('delete_grade/<int:grade_id>/', views.delete_grade, name='delete_grade'),

]
