from django.shortcuts import render
from cookies.forms import ProductForm
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

def addproduct(request):
    if request.method=="POST":
        name=request.POST.get("name")
        qty=request.POST.get('qty')
        res=render(request,"home.html",context={})
        res.set_cookie(name,qty)
        return res 
    form=ProductForm()
    res=render(request,"addproduct_temp.html",context={'form':form})
    return res


def viewcart(request):
    products={}
    for name,qty in request.COOKIES.items():
        if name!='csrftoken':
            products[name]=qty 


    res=render(request,"viewcart_temp.html",context={'products':products})
    return res 


def updateproduct(request):
    if request.method=="POST":
        name=request.POST.get("name")
        qty=request.POST.get('qty')
        res=render(request,"home.html",context={})
        res.set_cookie(name,qty)
        return res 
    form=ProductForm()
    res=render(request,"updateproduct_temp.html",context={'form':form})
    return res
def deleteproduct(request):
    if request.method=="POST":
        name=request.POST.get("name")
        res=render(request,"home.html",context={})
        res.delete_cookie(name)
        return res 
    form=ProductForm()
    res=render(request,"deleteproduct_temp.html",context={'form':form})
    return res

