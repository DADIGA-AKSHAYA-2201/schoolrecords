from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.getStudents, name='student_list'),
    path('add-student/', views.addStudent, name='add_student'),
    path('delete-student/<str:student_id>/', views.delete_student, name='delete_student'),
    path('update-student/<str:student_id>/', views.update_student, name='update_student'),
    
]
