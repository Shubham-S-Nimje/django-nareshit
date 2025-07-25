from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from doc.forms import DoctorForm,PatientForm,AppointmentForm
from doc.models import Doctor,Patient,Appointment
from django.urls import reverse 

# Create your views here.
def doctoradd(request):
    mesg=''
    if request.method=='POST':
        d=DoctorForm(request.POST)
        if d.is_valid():
            d.save()
            mesg="Doctor Details Added"
    
    form=DoctorForm()
    response=render(request,"adddoctor_temp.html",context={'form':form,'mesg':mesg})
    return response 

def listdoctors(request):
    qs=Doctor.objects.all()
    response=render(request,"listdoctors_temp.html",context={'qs':qs})
    return response 

def home(request):
    response=render(request,"base.html",context={})
    return response

def doctoredit(request,name):
    d=Doctor.objects.get(name=name) 
    if request.method=="POST":
        form=DoctorForm(request.POST,instance=d)
        if form.is_valid():
            form.save()
            response=redirect('doctorlist')
            return response 
    form=DoctorForm(instance=d)   
    response=render(request,"editdoctor_temp.html",context={'form':form})
    return response 

def doctordelete(request,name):
    qs=Doctor.objects.filter(name=name)
    qs.delete()
    res=redirect("doctorlist")
    return res 

def patientadd(request):
    msg=""
    if request.method=='POST':
        form=PatientForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Patient Details Saved"
    
    form=PatientForm()
    res=render(request,"patientadd_temp.html",context={'form':form,'msg':msg})
    return res 

def patientlist(request):
    qs=Patient.objects.all()
    res=render(request,"listpatient_temp.html",context={'qs':qs})
    return res 

def patientedit(request,name):
    d=Patient.objects.get(name=name) 
    if request.method=="POST":
        form=PatientForm(request.POST,instance=d)
        if form.is_valid():
            form.save()
            response=redirect('patientlist')
            return response 
    form=PatientForm(instance=d)   
    response=render(request,"editpatient_temp.html",context={'form':form})
    return response 

def patientdelete(request,name):
    p=Patient.objects.get(name=name)
    p.delete() 
    res=redirect('patientlist')
    return res 

def appointment(request):
    msg=""
    if request.method=="POST":
        d=Doctor.objects.get(name=request.POST.get('doctor'))
        p=Patient.objects.get(name=request.POST.get('patient'))
        date=request.POST.get('date')
        time=request.POST.get('time')
        desc=request.POST.get('desc')
        Appointment.objects.create(doctor=d,patient=p,date=date,time=time,description=desc)
        
        msg="Appointment is Confirmed"
    qs1=Doctor.objects.all() 
    qs2=Patient.objects.all() 
    res=render(request,"appointment_temp.html",context={'qs1':qs1,'qs2':qs2,'msg':msg})
    return res 

def applist(request):
    qs=Appointment.objects.all()
    res=render(request,"applist_temp.html",context={'qs':qs})
    return res