from django.shortcuts import render
from .models import StudentsModel
from students.forms import AddStudentForm

def students(request):
    students=StudentsModel.objects.all()
    # print(students)
    res=render(request,"students.html", context={'studentsList': students})
    return res

def add(request):
    if request.method=="POST":
        form=AddStudentForm(request.POST)
        print(form)
        if form.is_valid():
            res=render(request,"success.html",context={'msg':'input data is valid'})
            return res 
        else:
            res=render(request,"add.html",context={'form':form})
            return res 
    form=AddStudentForm()
    res=render(request,"add.html",context={'form':form})
    return res
    # res=render(request,"add.html", context={})
    # return res

def update(request):
    res=render(request,"update.html", context={})
    return res
def delete(request):
    res=render(request,"del.html", context={})
    return res
def listData(request):
    res=render(request,"list.html", context={})
    return res

def addstudent(request):
    rollno=request.GET.get('rollno')
    name=request.GET.get('name')
    course=request.GET.get('course')
    fees=request.GET.get('fees')
    print(rollno, name, course, fees)
    # StudentsModel.objects.create(rollo=rollno, name=name, course=course, fee=fees)
    res=render(request,"add.html", context={})
    return res

def modify(request):
    rollno=request.GET.get('rollno')
    course=request.GET.get('course')
    fees=request.GET.get('fees')
    student=StudentsModel.objects.get(rollo=rollno)
    student.course=course 
    student.fee=fees 
    student.save()
    # print(student)
    res=render(request,"update.html", context={})
    return res

def remove(request):
    rollno=request.GET.get('rollno')
    student=StudentsModel.objects.filter(rollo=rollno)
    student.delete()

    res=render(request,"del.html", context={})
    return res

def display(request):
    # rollno=request.GET.get('rollno')
    rollno = 101
    student=StudentsModel.objects.filter(rollo=rollno).first()
    print(student)
    res=render(request,"display.html", context={'studentDetails': student})
    return res
  