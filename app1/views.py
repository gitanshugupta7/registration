import datetime
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
import requests


# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    if request.method=='POST':
        ipv4=request.POST.get('ipv4')
        try:
            log_data = DailyAttendance.objects.get(user=request.user, date = datetime.date.today())
        except DailyAttendance.DoesNotExist:
            log_data = None

        emp = Employee.objects.get(user = request.user)
        if log_data == None:
            if emp.ipv4 == ipv4:
                log  = DailyAttendance(user = request.user, ipv4 = ipv4)
                log.save()
            else:
                return render(request, 'cannot.html')
        elif emp.ipv4 == ipv4:
            log_data.save()
        else:
            return render(request, 'cannot.html')

    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        company=request.POST.get('company')
        ipv4=request.POST.get('ipv4')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.first_name=firstname
            my_user.last_name=lastname
            my_user.save()
            company_o=Company.objects.get(companyName=company)
            employee=Employee.objects.create(user=my_user, company=company_o, ipv4=ipv4)
            employee.save()
            return redirect('login')
        
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')