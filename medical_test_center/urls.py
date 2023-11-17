"""medical_test_center URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from medical_test_center_app.views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', homepage, name='homepage'),
    path('login/', LoginView.as_view(), name='login'),
    path('tests/', tests, name='tests'),
    path('team/',biologists,name='biologists'),
    path('biologist/<int:biologistid>', display_biologist, name='show_biologist'),
    path('logout/', logoutview, name='logout'),
    path('medical-application-form/', MedicalApplicationFormView.as_view(), name='medical_application_form'),
    path('patients/',patients,name='patients')

]
