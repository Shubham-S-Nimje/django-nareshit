from django.shortcuts import render

def homePage(request):
    response = render(request, 'index.html', context={})
    return response
def courses(request):
    response=render(request,"courses.html")
    return response 
def about(request):
    response=render(request,"about.html")
    return response 
def contacts(request):
    response=render(request,"contacts.html")
    return response  