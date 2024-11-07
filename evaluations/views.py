from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Faculty, Grade
from .forms import StudentForm, FacultyForm, GradeForm  # Import the student form


# Create your views here.
def getStudents(request):
    all_students = Student.objects.all()
    context = {'students': all_students}
    # Render the template with the context
    return render(request, 'student_list.html', context)

def addStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to student list page after successful submission
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')  # Redirect to student list page after successful deletion
    return render(request, 'delete_student.html', {'student': student})

def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to student list page after successful update
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form, 'student': student})
