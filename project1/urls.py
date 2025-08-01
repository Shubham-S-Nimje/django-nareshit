"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from app1.views import *
from calculator.views import *
from students.views import *
from doc.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='home'),
    path('about/', about, name='about'),
    path('courses/', courses, name='courses'),
    path('contacts/', contacts, name='contacts'),
    path('calculator/', calculator, name='calculator'),
    path('students/', students, name='students'),
    path('register/', register, name='register'),

    path('students/add/', add, name='add students'),
    path('students/update/', update, name='update students'),
    path('students/delete/', delete, name='delete students'),
    path('students/list/', listData, name='list students'),
    
    path('students/addstudent/', addstudent, name='add students'),
    path('students/modify/', modify, name='modify students'),
    path('students/remove/', remove, name='remove students'),
    path('students/display/', display, name='display students'),

    path('doc/', include('doc.urls')),
    path('cookies/', include('cookies.urls')),
]
