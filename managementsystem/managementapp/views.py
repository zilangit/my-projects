from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from managementapp.models import City, Course, Managment


# Create your views here.
def reg_fun(request):
    return render(request,'register.html',{'data':''})


def regdata_fun(request):

    user_name= request.POST['txtusername'] #for reading the register.html data!
    user_email = request.POST['txtuseremail']
    user_pswd = request.POST['pwdpass']
    if User.objects.filter(Q(username= user_name)|Q(email=user_email)).exists():
        return render(request,'register.html',{'data' : 'Username,email and password Already exist'})
    else:
        u1 = User.objects.create_superuser(username= user_name,email=user_email,password=user_pswd)
        u1.save()
        return redirect(request,'log')


def log_fun(request):
    return render(request,'login.html',{'data':''})


def logdata_fun(request):
    user_name = request.POST['txtname']
    user_pswd = request.POST['pwdpass']
    # if User.objects.filter(username=user_name, password=user_pswd).exists:
    # else:
    #     return render(request, 'login.html', {'data': 'Login details Invalid'})

    user1= authenticate(username=user_name, password=user_pswd)#it is used to compare user table!
    if user1 is not None:
        if user1.is_superuser:
            # login(user1)
            return redirect('home')
        else:
            return render(request,'login.html',{'data':'User is not a super user'})
    else:
        return render(request,'login.html',{'data':'Enter proper username and password'})


def home_fun(request):
    return render(request,'home.html')


def add_fun(request):
    city=City.objects.all()
    course = Course.objects.all()

    return render(request,'addstudent.html',{'City_Data': city ,'Course_Data':course})


def readdata_fun(request):
    s1=Managment()
    s1.Man_Name=request.POST['txtusername']
    s1.Man_Age=request.POST['numage']
    s1.Man_Phone=request.POST['numphn']
    s1.Man_City=City.objects.get(City_Name=request.POST['ddlcity'])
    s1.Man_Course=Course.objects.get(Course_Name=request.POST['ddlcourse'])
    s1.save()
    return redirect('add')



def diplay_fun(request):
    s1=Managment.objects.all()

    return render(request,'display.html',{'data':s1})


def update_fun(request,id):
    s1=Managment.objects.get(id=id)
    city =City.objects.all() #it will get all city in update page to update!
    course =Course.objects.all()

    if request.method=='POST':
        s1.Man_Name = request.POST['txtusername']
        s1.Man_Age = request.POST['numage']
        s1.Man_Phone = request.POST['numphn']
        s1.Man_City = City.objects.get(City_Name=request.POST['ddlcity'])
        s1.Man_Course = Course.objects.get(Course_Name=request.POST['ddlcourse'])
        s1.save()
        return redirect('display')
    return render(request,'update.html',{'data':s1,'City_Data':city,'Course_Data':course})


def delete_fun(request,id):
    s1=Managment.objects.get(id=id)
    s1.delete()
    return redirect('display')


def logout_fun(request):
    return redirect('log')