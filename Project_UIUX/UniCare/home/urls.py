from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('Patient',views.home,name='home'),
     path('Doctor',views.home,name='home'),
    path('DSignup',views.doctorsignup,name='doctorsignup'),
    path('PSignup',views.patientsignup,name='patientsignup'),
    path('PLogin',views.patientlogin,name='patientlogin'),
    path('DLogin',views.doctorlogin,name='doctorlogin'),
    path('PLogin/uploaddoc.html',views.Upload,name='uploaddocument'),
    path('PLogin/viewDocument.html',views.viewdocs,name='viewdocs'),
    path('DLogin/viewDocument1.html',views.viewdocs1,name='viewdocs1'),
    path('PDashboard',views.patientdashboard,name='patientdashboard'),
    path('DDashboard',views.doctordashboard,name='doctordashboard')
    # path('PLogin/Docupload',views.uploaddoc,name='uploaddoc')
    # PLogin/Docupload
]
