from django.shortcuts import render,redirect
from home.models import Patient,Doctor,Uniqueid,Document
from django.template import Template, Context
from django.http import HttpResponse
import random
# from django.contrib.auth.hashers import make_password

# from django.shortcuts import render
from json import dumps
# class counter:
#    c=1000
#    ins3=Uniqueid(UniqueID=c)
#    ins3.save
# ob=counter()
def home(request):
    return render(request, 'index.html')


def doctorsignup(request):
    num = random.randint (0,99999)
    if request.method == "POST":
        print("POST REQUEST ACCEPTED")

        DFirstname = request.POST['firstname']
        DLastname = request.POST['lastname']
        DDate_of_Birth = request.POST['date-of-birth']
        # Blood_Group = request.POST['blood-group']
        DContact_Number = request.POST['contact-number']
        DEMail = request.POST['e-mail']
        DGender=request.POST['gender']
        DSpeciality=request.POST['Speciality']
        Password = request.POST['password']
        Confirm_Password = request.POST['confirm-password']
        iddd=id(DFirstname)
        UniqueID=int(str(iddd)[:5])
        UniqueID=int(str(UniqueID+num)[:5])
        print(UniqueID)
        # Unique_ID=
        ins2 = Doctor(Firstname=DFirstname, Lastname=DLastname, Date_of_Birth=DDate_of_Birth,
                      Contact_Number=DContact_Number, EMail=DEMail,Gender=DGender,Speciality=DSpeciality,Password=Password, Confirm_Password=Confirm_Password,UniqueID= UniqueID)
        ins2.save()
        del UniqueID
        print("CONGO! DATA WRITTEN")
        response = redirect('/DLogin')
        return response
    return render(request, 'signup_doctor.html')


def patientsignup(request):
    num = random.randint (0,99999)
    if request.method == "POST":
        print("POST REQUEST ACCEPTED")
        Firstname = request.POST['firstname']
        Lastname = request.POST['lastname']
        Date_of_Birth = request.POST['date-of-birth']
        Blood_Group = request.POST['blood-group']
        Contact_Number = request.POST['contact-number']
        EMail = request.POST['e-mail']
        Gender=request.POST['gender']
        Password = request.POST['password']
        Confirm_Password = request.POST['confirm-password']
# set authentication if user already exists
        idd=id(Firstname)
        UniqueID=int(str(idd)[:5])
        UniqueID=UniqueID+num
        print(UniqueID)
        ins = Patient(Firstname=Firstname, Lastname=Lastname, Date_of_Birth=Date_of_Birth, Blood_Group=Blood_Group,
                      Contact_Number=Contact_Number, EMail=EMail,Gender=Gender,Password=Password, Confirm_Password=Confirm_Password, UniqueID= UniqueID)
        # print("COUNTER VALUE IS:")
        # print(Uniqueid(UniqueID))
        ins.save()
        del UniqueID
        print("CONGO! DATA WRITTEN")
        response = redirect('/PLogin')
        return response
    return render(request, 'signup_patient.html')
EmA=None
PaS=None

def patientlogin(request):
    allpatients = Patient.objects.all()
    if request.method == "POST":
        print("IN login")
        l_Email = request.POST['e-mail']
        l_Pass = request.POST['password']
        global EmA
        global PaS
        def EmA():
          return l_Email
        def PaS():
          return l_Pass
        
        print("I AM ON LOGIN PAGE")
        for p in allpatients:
            if l_Pass == p.Password and l_Email == p.EMail:
                #   print("SUCCESS",p.Firstname)
                # context = {}
                print("yes")
                # dataDictionary = {
                #     'Unique_id':p.UniqueID,
                #     'Gender': p.Gender,
                #     'blood' : p.Blood_Group,
                #     'Contact' : p.Contact_Number,
                #     'Date_of_birth' : p.Date_of_Birth,
                #     'Email':p.EMail,
                #     }
    # dump data
                # dataJSON = dumps(dataDictionary)
    # dataJSON = dumps(dataDictionary)
                # return render(request, 'dashboard.html',{'name': p.Firstname,'data': dataJSON})  yeh puraana dashboard tha
                # return render(request,'/PDashboard',{'name': p.Firstname,'data': dataJSON})
                return redirect('/PDashboard')
                
    #  print("RUN SUCCESS")
    #  print(l_Email,l_Pass)

    # if l_email ==
    return render(request, 'login_patient.html')
def patientdashboard(request):
    print("I AM ON Dashboard")
    allpatients = Patient.objects.all()
    if request.method == "POST":
        Email=request.POST['Email']
        name = request.POST['Name']
        date = request.POST['Date']
        images = request.FILES.getlist('photos')
        print(images)
        for p in allpatients:
            if Email==p.EMail:
                Uniqueid=p.UniqueID
                for f in images:
                 ins3=Document(Email=Email,Name=name,Date=date,Images=f,Uniqueid=Uniqueid)
                 ins3.save()
                return HttpResponse("Files Uploaded Successfully")
        return HttpResponse("Email not found") 
    l_Email=EmA()
    l_Pass=PaS()
    for p in allpatients:
            if l_Pass == p.Password and l_Email == p.EMail:
                dataDictionary = {
                    'Unique_id':p.UniqueID,
                    'Gender': p.Gender,
                    'blood' : p.Blood_Group,
                    'Contact' : p.Contact_Number,
                    'Date_of_birth' : p.Date_of_Birth,
                    'Email':p.EMail,
                    }
                dataJSON = dumps(dataDictionary)
                return render(request,'dashboard.html',{'name': p.Firstname,'data': dataJSON})
    
DEmA=None
DPaS=None

def doctorlogin(request):
    alldoctors = Doctor.objects.all()
    if request.method == "POST":
        print("IN login")
        l_Email = request.POST['e-mail']
        l_Pass = request.POST['password']
        global DEmA
        global DPaS
        def DEmA():
          return l_Email
        def DPaS():
          return l_Pass
        
        print("I AM ON LOGIN PAGE")
        for d in alldoctors:
            if l_Pass == d.Password and l_Email == d.EMail:
                print("SUCCESS",d.Firstname)
                print(l_Email,l_Pass)
                return redirect('/DDashboard')
             
    #             dataDictionary = {
    #                 'Unique_id': 'P00',
    #                 'Gender': 'Male',
    #                 'blood' : p.Blood_Group,
    #                 'Contact' : p.Contact_Number,
    #                 'Date_of_birth' : p.Date_of_Birth
    #             }
    # # dump data
    #             dataJSON = dumps(dataDictionary)
    # dataJSON = dumps(dataDictionary)
             
                # return render(request, 'dashboard.html',{'data': dataJSON})
    #  print("RUN SUCCESS")
    #  print(l_Email,l_Pass)

    # if l_email ==
    return render(request, 'login_doctor.html')

yoyo=None
def doctordashboard(request):
    print("I AM ON Dashboard")
    alldoctors = Doctor.objects.all()
    allpatients=Patient.objects.all()
    if request.method == "POST":
        if 'upload' in request.POST:
            print("i am in upload")
            UIDe=request.POST['uid']
            name = request.POST['udname']
            date = request.POST['udate']
            im = request.FILES.getlist('xyz')
            print(im)
            print(UIDe+name+date)
            for p in allpatients:
                if UIDe==p.UniqueID:
                    Email=p.EMail
                    for f in im:
                     ins4=Document(Email=Email,Name=name,Date=date,Images=f,Uniqueid=UIDe)
                     ins4.save()
                    return HttpResponse("Files Uploaded Successfully")
            return HttpResponse("UID not found") 
        elif 'view' in request.POST:
            print("inview")
            UIDv=request.POST['pID']
            global yoyo
            def yoyo():
                return UIDv
            return redirect('/DLogin/viewDocument1.html')
            # return render(request,'viewDocument1.html',{'id':UIDv})
            
    l_Email=DEmA()
    l_Pass=DPaS()
    for d in alldoctors:
            if l_Pass == d.Password and l_Email == d.EMail:
                dataDictionary = {
                    'Unique_id':d.UniqueID,
                    'Gender': d.Gender,
                    'speciality' : d.Speciality,
                    'Contact' : d.Contact_Number,
                    'Date_of_birth' : d.Date_of_Birth,
                    'Email':d.EMail,
                    }
                dataJSON = dumps(dataDictionary)
    return render(request,'doctor_dashboard.html',{'name': d.Firstname,'data': dataJSON})


# def uploaddoc(request):
#         return render(request,'uploaddoc.html')

def Upload(request):
    allpatients = Patient.objects.all()
    if request.method == "POST":
        Email=request.POST['Email']
        name = request.POST['Name']
        date = request.POST['Date']
        images = request.FILES.getlist('photos')
        for p in allpatients:
            if Email==p.EMail:
                Uniqueid=p.UniqueID
                for f in images:
                 ins3=Document(Email=Email,Name=name,Date=date,Images=f,Uniqueid=Uniqueid)
                 ins3.save()
                return HttpResponse("Files Uploaded Successfully")
        return HttpResponse("Email not found") 
        
        
        
    # response = redirect('/PLogin/Docupload')
    # return response
    return render(request,'uploaddoc.html')



def viewdocs(request):
    alldocs = Document.objects.all()
    data=[]
    for d in alldocs:
     path=d.Images.path
     path=str(path)[53:]
    #  print(path)
     dataDictionary = {
                    'Unique_id':d.Uniqueid,
                    'title':d.Name,
                    'date':d.Date,
                    'image':path
                    }
     data.append(dataDictionary)
    print(data)
    dataJSON = dumps(data)
    data.clear()
    return render(request,'viewDocument.html',{'data':dataJSON})

def viewdocs1(request):
    alldocs = Document.objects.all()
    data=[]
    for d in alldocs:
     path=d.Images.path
     path=str(path)[53:]
    #  print(path)
     dataDictionary = {
                    'Unique_id':d.Uniqueid,
                    'title':d.Name,
                    'date':d.Date,
                    'image':path
                    }
     data.append(dataDictionary)
    print(data)
    dataJSON = dumps(data)
    data.clear()
    IID=yoyo()
    return render(request,'viewDocument1.html',{'link':IID,'data':dataJSON})
    # return render(request,'viewDocument.html')
# Create your views here.
