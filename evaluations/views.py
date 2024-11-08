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

def faculty_list(request):
    all_faculties = Faculty.objects.all()
    context = {'faculties': all_faculties}
    # Render the template with the context
    return render(request, 'faculty_list.html', context)

def add_faculty(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')
    else:
        form = FacultyForm()
    return render(request, 'add_faculty.html', {'form': form})

def update_faculty(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        form = FacultyForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')
    else:
        form = FacultyForm(instance=faculty)
    return render(request, 'update_faculty.html', {'form': form, 'faculty': faculty})

def delete_faculty(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        faculty.delete()
        return redirect('faculty_list')
    return render(request, 'delete_faculty.html', {'faculty': faculty})

def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to student list page after successful submission
    else:
        form = GradeForm()
    return render(request, 'add_grade.html', {'form': form})


def view_grades(request, student_id):
    grades = Grade.objects.filter(student_id=student_id)
    student_name = grades.first().student.first_name + ' ' + grades.first().student.last_name  # Get student name
    context = {
        'student_name': student_name,
        'grades': grades
    }
    return render(request, 'view_grades.html', context)

def update_grade(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('view_grades', student_id=grade.student.id)
    else:
        form = GradeForm(instance=grade)
    return render(request, 'update_grade.html', {'form': form})

def delete_grade(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    if request.method == 'POST':
        grade.delete()
        return redirect('view_grades', student_id=grade.student.id)
    return render(request, 'delete_grade.html', {'grade': grade})
