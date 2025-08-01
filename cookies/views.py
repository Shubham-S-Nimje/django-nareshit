from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def view1(request):
    name=request.GET.get('name')
    link="<a href='/cookies/find'>Find My Name </a>"
    response=HttpResponse(link) 
    response.set_cookie('name',name)
    return response 


def view2(request):
    name=request.COOKIES.get('name')
    res=HttpResponse("Your Name is "+name +"👌")
    return res 


def home(request):
    response=render(request,"home.html",context={})
    return response 