import email
from pyexpat.errors import messages
import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.models import authenticate,login,logout

# Create your views here.
def home(request):
    # return HttpResponse("Hello your project is working")
    return render(request, "authentication/index.html")

def signup(request):
    if  request.method == "POST":
        username=request.POST["username"]
        fname=request.POST["firstname"]
        lname=request.POST["lastname"]
        email=request.POST["email"]
        pass1=request.POST["password"]
        pass2=request.POST["confirm password"]

        myuser= User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name =  lname
        myuser.confirm = pass2
        myuser.save()
        messages.success(request,"Your account has been succesfully created!")
        return redirect("signin")

    return render(request, "authentication/signup.html")

def signin(request):
    if request.method == "POST":
       username = request.POST["username"] 
       pass1 = request.post["pass1"]


       user = authenticate(username=username,password=pass1)

       if user is not None:
         login(request,user)
         fname = user.first_name
         return render(request,"authentication/index.html",{"fname":fname} )

       else:
            messages.error(request,"You have entered wrong credentials")
            return redirect("home")



    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out succesfully")
    return redirect("home")