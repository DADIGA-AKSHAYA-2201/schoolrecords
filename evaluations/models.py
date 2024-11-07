from django.db import models

class Student(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    parent_contact_info = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Faculty(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Grade(models.Model):
    id = models.IntegerField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.CharField(max_length=50)
    teacher = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f"{self.student} - {self.course} - {self.grade}"