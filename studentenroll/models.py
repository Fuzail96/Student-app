from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    TeachId=models.CharField(max_length=20, auto_created=True, null=False, primary_key=True)
    Name=models.CharField(max_length=40)
    email=models.EmailField()
    contact=models.CharField(max_length=40)

    def __str__(self):
        return str(self.Name)


class Course(models.Model):
    CourseId=models.CharField(max_length=20, auto_created=True, null=False, primary_key=True)
    c_name=models.CharField(max_length=40)
    teacher=models.OneToOneField(Teacher, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.c_name)


class StuCourses(models.Model):
    Courses=models.ForeignKey(Course, unique=False, on_delete=models.CASCADE)
    Student=models.ForeignKey(User, unique=False, on_delete=models.CASCADE)








