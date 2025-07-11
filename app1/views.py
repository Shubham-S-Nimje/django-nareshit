from django.shortcuts import render
from app1.forms import StudentForm, RegisterForm

def homePage(request):
    # ================v1======================
    email_list=['nareshit@nareshit.com',
    'ramesh@gmail.com',
    'kishore@gamil.com',
    'rajesh@gmail.com']
    # =================v2=====================
    marks={'naresh':[40,50,60],
    'ramesh':[60,70,80],
    'suresh':[70,80,90]}
    # =================v3=====================
    A=[10,20,30,40,50]
    B={'x':10,'y':20,'z':30}

    response = render(request, 'index.html', context={'email_list':email_list,'marks':marks,'A':A,'B':B})
    return response


    # =================register=====================
    flag=True


# def email_validator(request):
#     if request.method=="POST":
#         form=RegisterForm(request.POST)
#         if form.is_valid():
#             res=render(request,"valid_temp.html",context={'msg':'input data is valid'})
#             return res 
#         else:
#             res=render(request,"email_temp.html",context={'form':form})
#             return res 
#     form=RegisterForm()
#     res=render(request,"email_temp.html",context={'form':form})
#     return res 

flag=True
def register(request):
    global flag 
    if flag:
        form=RegisterForm()
        res=render(request,"register.html",context={'form':form}) 
        flag=False 
        return res 
    else:
        form=RegisterForm(request.GET)
        if form.is_valid():
            uname=form.cleaned_data['username']
            print(f'{uname} registeration completed')
        else: 
            res=render(request,"register.html",context={'form':form})   
            return res 
        form=RegisterForm()
        res=render(request,"register.html",context={'form':form})
        return res 
    
def about(request):
    response=render(request,"about.html")
    return response 

def contacts(request):
    a = 'ironman'
    b = 'thor'
    c =  'deadpool'
    # response=render(request,"contacts.html", context={'a':a,'b':b,'c':c})

    if request.method == 'POST':
        studform = StudentForm(request.POST)
        if studform.is_valid():
            print(studform.cleaned_data)
            return render(request, "success.html", {'form': studform.cleaned_data})
        else:
            response=render(request,"contacts.html",context={'a':a,'b':b,'c':c, 'studform':studform})
            return response
    else:
        studform = StudentForm(request.POST)
        response=render(request,"contacts.html",context={'a':a,'b':b,'c':c, 'studform':studform})
        return response 

def courses(request):
    a = 'python'
    b = 'django'
    c = 'flask'
    response=render(request,"courses.html", context={'a':a,'b':b,'c':c})
    return response 