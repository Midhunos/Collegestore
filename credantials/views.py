from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.
def Login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("index2")
        else:
            messages.info(request,"invalid credentials")
            return redirect("log")


    return render(request,"login.html")
def Register(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        cpassword=request.POST["cpassword"]

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Already exists")
                return redirect("reg")
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect("reg")
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();

                return redirect("log")
        else:
            messages.info(request,"Password not matching")
            return redirect("reg")
        return redirect("/")
    return render(request,"register.html")

def Logout(request):
    auth.logout(request)
    return redirect("/")