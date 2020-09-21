from django.contrib import admin
from .models import Course, Teacher, StuCourses

# Register your models here.
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(StuCourses)
