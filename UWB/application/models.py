from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    index_number = models.CharField(max_length=45)

class Lecturer(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

class Classes(models.Model):
    name = models.CharField(max_length=45)
    lecturer = models.ForeignKey('Lecturer')

class Attendance(models.Model):
    date = models.DateTimeField()
    attend = models.BooleanField(default=False)
    student = models.ForeignKey('Student')
    lecturer = models.ForeignKey('Lecturer')
    classes = models.ForeignKey('Classes')

