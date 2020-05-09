from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate
from .models import All_Patients,Old_Patients
from django.contrib import messages 
from django.template import Context,Template
import mysql.connector
from django.db.models import Count
from datetime import datetime

from .forms import All_Patients_Form


# for trimming the text
# import re





# Create your views here.

def login(request):
    if request.method=='POST':
        username = request.POST.get('phone')
        password = request.POST.get('pass')

        


        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,"Welcome Doctor have a nice day")
            return render(request,'newform.html')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect("login")

    else:
        return render(request,'HomePage.html')

def forgotpassword(request):
    if request.method=='POST':
        Key = request.POST.get('key')
        un = request.POST['uname']
        np = request.POST['npassword']
        cp = request.POST['cpassword']
        if(Key == '78457'):
            if np == cp:
                if User.objects.filter(username=un).exists():
                    s_user = User.objects.get(username=un)
                    s_user.set_password(np)
                    s_user.save()
                    messages.success(request,'Password has been reset successfully. ')
                    return render(request,"HomePage.html")
                    
                else:
                    messages.error(request,'Username not found ')
                    return render(request,"forgotpassword.html")
            else:
                messages.error(request,'Password mismatch')
                return render(request,"forgotpassword.html")  
        else:
            messages.error(request,'Invalid Key')
            return render(request,"forgotpassword.html") 

    else:
        
        return render(request,'forgotpassword.html')


def Logout(request):
    auth.logout(request)
    messages.success(request,"Logout Successfull")
    return redirect("login")



def newform(request):
    return render(request,'newform.html')


 
def Old_Patient(request,id):
    patient = All_Patients.objects.get(id=id)
    return render(request, 'Old_Patient.html', {'patient': patient})


    
def Old_Patient2(request): 
    return render(request, 'Old_Patient.html')

        


def data(request):
    return render(request,'data.html')

def NewPatient(request):
    if request.method=='POST':
        F_name = request.POST.get('Fname')
        Gender = request.POST.get('sex')
        Date = request.POST.get('Date')

        

        Mo_no = request.POST.get('Mo_no')
        Age = request.POST.get('age')

        total_fee = request.POST.get('TotFee')
        paid_fee = request.POST.get('GivenFee')
        pending_fee = request.POST.get('Pending')

        final_dignosis = request.POST.get('final_digno')
        blood_pressure = request.POST.get('blood_press')

        temp_add = request.POST.get('temp_add')
        parme_add = request.POST.get('parme_add')
        parme_disease = request.POST.get('Parme_dise')
        ipd = request.POST.get('ipd')


        Cc = request.POST.get('Cc')   
        Aller = request.POST.get('Aller')
        Pd = request.POST.get('Pd')
        Treat = request.POST.get('Treat')
        # causing problem 
        Cn = request.POST.get('Cn','') 

        obj = All_Patients.objects.filter(fname = F_name)

       
        if (obj):
            messages.error(request,'Duplicate Patient name Exists !')
            
            
            
            return redirect('Old_Patient2')
        else:
            # for old patient entry
            PatientEntry2 = Old_Patients(fname=F_name,date=Date,age=Age,final_digno=final_dignosis,blood_press=blood_pressure,total_fee=total_fee,given_fee=paid_fee,remaining_fee=pending_fee,cheapcomp=Cc,allergy=Aller,provisdigno=Pd,treatment=Treat,clinicalnotes=Cn,temporary_add=temp_add,parmanent_add=parme_add,parmanent_disease=parme_disease,ipd=ipd)
            PatientEntry2.save()
            # for new patient entry
            Patient = All_Patients(fname=F_name,gender=Gender,date=Date,mo_no=Mo_no,age=Age,final_digno=final_dignosis,blood_press=blood_pressure,cheapcomp=Cc,allergy=Aller,provisdigno=Pd,treatment=Treat,clinicalnotes=Cn)        
            Patient.save()
            messages.success(request,'Patient Added Successfully !') 

            # calling print function 

            last_patient = All_Patients.objects.latest()
    
            last_id = last_patient.id

            print(last_id)
            return redirect('Print_for_all',id=last_id)
            
    else:
        return render(request,'newform.html')












# for printing any patient info
def PrintAny(request):
    if (request.method == 'POST'):
        name = request.POST.get('Name')
        patient = All_Patients.objects.filter(fname = name)
        if not patient:
            
            messages.error(request,'This Patient doesent exists !')
            return redirect('PrintIt')
        else:  
            
            messages.success(request,'Its Present')



        return render(request,'PrintData.html',{'patient':patient})

    else:
        return render(request,'PrintIt')

# for printing  patient
def Print_for_all(request,id):
    patient = All_Patients.objects.filter(id=id)
    return render(request,'PrintData.html',{'patient':patient})


      
    
        








def AllPatient(request):
    patient = All_Patients.objects.all()

    Total_patients = All_Patients.objects.count()

    print(Total_patients)

    return render(request,'AllPatients.html', {'patient': patient,'Total_patients': Total_patients})

 
def edit_patient(request, id):
    patient = All_Patients.objects.get(id=id)
    print(patient)
    return render(request, 'editnew.html', {'patient': patient})


# after editing the control would come to here

def update(request, id):
    print(id)
    if request.method=='POST':
        F_name = request.POST.get('Fname')
        Gender = request.POST.get('sex')
        Date = request.POST.get('Date')
        Mo_no = request.POST.get('Mo_no')
        Age = request.POST.get('age')


        Cc = request.POST.get('Cc')
        
        Aller = request.POST.get('Aller')
        Pd = request.POST.get('Pd')
        Treat = request.POST.get('Treat')
        # causing problem 
        Cn = request.POST.get('Cn','') 

        final_dignosis = request.POST.get('final_digno')
        blood_pressure = request.POST.get('blood_press')


        

        All_Patients.objects.filter(id=id).update(fname=F_name,gender=Gender,date=Date,mo_no=Mo_no,age=Age,final_digno=final_dignosis,blood_press=blood_pressure,cheapcomp=Cc,allergy=Aller,provisdigno=Pd,treatment=Treat,clinicalnotes=Cn)
           
        messages.success(request,'Patient info updated Successfully !')
        return redirect('AllPatient')            
    else:
        return render(request,'AllPatients.html')


def delete_patient(request, id):
    patient = All_Patients.objects.get(id=id)
    patient.delete()
    messages.success(request,'Patient deleted Successsfully')
    return redirect('AllPatient')




# -------------------For CRUD of Old Patients--------------------------


def OldPatient(request):
    return render(request,'Old_Patient.html')


#for printing history of specific patient

def All_detail(request,id):

    #fetching fname with help of id
    object = All_Patients.objects.get(id=id)

    Fname = object.fname

    print(Fname)

    #filtering the records from old_patients with same name
    patient = Old_Patients.objects.filter(fname = Fname)

    return render(request,'Every_Detail.html', {'patient': patient ,'Fname': Fname})

# Editing

def edit_oldpatient(request, id):
    patient = Old_Patients.objects.get(id=id)
    return render(request, 'editold.html', {'patient': patient})


# after editing control would come to here

def update_old(request, id):
    print(id)
    if request.method=='POST':  
        F_name = request.POST.get('Fname')
        
        Date = request.POST.get('Date')
        
       

        total_fee = request.POST.get('TotFee')
        paid_fee = request.POST.get('GivenFee')
        pending_fee = request.POST.get('Pending')

        Cc = request.POST.get('Cc')


        final_dignosis = request.POST.get('final_digno')
        blood_pressure = request.POST.get('blood_press')

        temp_add = request.POST.get('temp_add')
        parme_add = request.POST.get('parme_add')
        parme_disease = request.POST.get('Parme_dise')
        ipd = request.POST.get('ipd')

        
        Aller = request.POST.get('Aller')
        Pd = request.POST.get('Pd')
        Treat = request.POST.get('Treat')
        # causing problem 
        Cn = request.POST.get('Cn','') 


        

        Old_Patients.objects.filter(id=id).update(fname=F_name,date=Date,total_fee=total_fee,given_fee=paid_fee,remaining_fee=pending_fee,final_digno=final_dignosis,blood_press=blood_pressure,cheapcomp=Cc,allergy=Aller,provisdigno=Pd,treatment=Treat,clinicalnotes=Cn,temporary_add=temp_add,parmanent_add=parme_add,parmanent_disease=parme_disease,ipd=ipd)
           
        messages.success(request,'Patient info updated Successfully !')
          
        return All_detail2(request,id)       
    else:
        return render(request,'Every_Detail.html')


def All_detail2(request,id):

    # getting object with id 
    obj = Old_Patients.objects.get(id=id)
    # getting fname with object
    Fname = obj.fname
    
    #filtering the records from old_patients with same name
    patient = Old_Patients.objects.filter(fname = Fname)

    return render(request,'Every_Detail.html', {'patient': patient})



# for printing by button of specific patient
def Print_for_all_2(request,id):
    patient = Old_Patients.objects.filter(id=id)
    return render(request,'PrintData.html',{'patient':patient})


def InsertRow(request):
    if request.method=='POST':
        F_name = request.POST.get('Fname')
        
        Date = request.POST.get('Date')
        
        Age = request.POST.get('age')

        total_fee = request.POST.get('TotFee')
        paid_fee = request.POST.get('GivenFee')
        pending_fee = request.POST.get('Pending')

        final_dignosis = request.POST.get('final_digno')
        blood_pressure = request.POST.get('blood_press')

        temp_add = request.POST.get('temp_add')
        parme_add = request.POST.get('parme_add')
        parme_disease = request.POST.get('Parme_dise')
        ipd = request.POST.get('ipd')

        Cc = request.POST.get('Cc')   
        Aller = request.POST.get('Aller')
        Pd = request.POST.get('Pd')
        Treat = request.POST.get('Treat')
        # causing problem 
        Cn = request.POST.get('Cn','') 

        obj = Old_Patients.objects.filter(fname = F_name)

        

       
        if (obj):
            Patient = Old_Patients(fname=F_name,date=Date,age=Age,total_fee=total_fee,given_fee=paid_fee,remaining_fee=pending_fee,final_digno=final_dignosis,blood_press=blood_pressure,cheapcomp=Cc,allergy=Aller,provisdigno=Pd,treatment=Treat,clinicalnotes=Cn,temporary_add=temp_add,parmanent_add=parme_add,parmanent_disease=parme_disease,ipd=ipd)        
            Patient.save()
            messages.success(request,'Patient\'s New Record Added Successfully !') 

            pt = Old_Patients.objects.latest('id')

            last_id = pt.id

            return redirect('Print_for_all_2',id=last_id)

            
            
        else:
            messages.error(request,'Please Add Patient first')
            return redirect('NewPatient')

    else:
        return render(request,'Old_Patient.html')



