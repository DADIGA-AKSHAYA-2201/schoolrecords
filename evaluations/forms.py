from django import forms
from .models import Student, Faculty, Grade

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'  # You can specify specific fields if needed


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'
        
class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'