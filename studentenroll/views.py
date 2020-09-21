from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .models import StuCourses, Course
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "welcome.html")


@login_required(login_url='/login')
def enroll(request):
    crs = Course.objects.all
    return render(request, "enroll.html", {"course":crs})


def add(request):
    inp1 = request.POST['courses']
    inp2 = request.POST['student']
    if inp2==request.user.email:
        cour = Course.objects.get(c_name=inp1)
        if StuCourses.objects.filter(Courses=cour).exists():
            messages.info(request, 'Course Already Enrolled')
            return redirect('enroll')
        else:
            stu = User.objects.get(email=inp2)
            StCour = StuCourses.objects.create(Courses=cour, Student=stu)
            StCour.save()
            return redirect('show')
    else:
        messages.info(request, 'Invalid Email')
        return redirect('enroll')


@login_required(login_url='/login')
def show(request):
    uId = request.user.id
    student = StuCourses.objects.filter(Student=uId)
    crs=[]
    for s in student:
        c = Course.objects.get(CourseId=s.Courses_id)
        crs.append(c)
    return render(request, 'show.html', {'student': crs})


def search(request):
    given_name = request.POST['name']
    student = StuCourses.objects.filter(fName__icontains=given_name)
    return render(request, 'show.html', {'student': student})


def register(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['re_password']

            if password == password2:
                if User.objects.filter(username=name).exists():
                    messages.info(request, 'Name Already In Use')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email Already In Use')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=name, email=email, password=password)
                    user.save()
                    subject = "Welcome"
                    message = ("Welcome to CodeArdents.\n"
                               + "Thanks for registering with us. \nNow you can explore the "
                               + "available cources and can enroll.\n\n\n"
                               + "Regards, \n CodeArdents")
                    from_email = settings.EMAIL_HOST_USER
                    to_list = [user.email]
                    send_mail(subject, message, from_email, to_list, fail_silently=True)
                    messages.info(request, "Thanks For Registering.")
                    return redirect('register')
            else:
                messages.info(request, 'Password Not Matching')
                return redirect('register')

        else:
            return render(request, 'register.html')
    except Exception as e:
        return ("Error:" + str(e) + "All Fields Are Required")


def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        user = auth.authenticate(username=name, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        elif user is None:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def course(request):
    return render(request, 'course.html')
