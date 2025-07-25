from django.contrib import admin
from django.urls import path
from doc.views import * 

urlpatterns = [
    path('', home),
    path('doctoradd/',doctoradd,name='doctoradd'),
    path('doctorlist/',listdoctors,name='doctorlist'),
    path('doctoredit/<name>/',doctoredit,name='doctoredit'),
    path('doctordelete/<name>/',doctordelete,name='doctordelete'),
    path('patientadd/',patientadd,name='patientadd'),
    path('patientlist/',patientlist,name='patientlist'),
    path('patientedit/<name>/',patientedit,name='patientedit'),
    path('patientdelete/<name>/',patientdelete,name='patientdelete'),
    path('appointment/',appointment,name='appointment'),
    path('applist/',applist,name='applist')
]
