from django.contrib import admin
from django.urls import path
from cookies.views import * 

urlpatterns = [
    path('', home),
    path('find/',view2),
    path('read/',view1),
]
