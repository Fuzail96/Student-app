from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('enroll', views.enroll, name='enroll'),
    path('add', views.add, name='add'),
    path('show', views.show, name='show'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('course', views.course, name='course'),


]