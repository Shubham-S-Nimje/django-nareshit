from django.shortcuts import render

def students(request):
    res=render(request,"students.html")
    return res
