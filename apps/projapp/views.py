from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
import bcrypt
from .models import *
#############################home###############################
def index(request):
    return render(request,"projapp/home.html")
#############################login###############################
def login(request): 
    return render(request, "projapp/login.html")
#############################logout###############################
def logout(request):
    del request.session['user']
    return redirect("/")
#############################login_process###############################
def login_process(request):
        user = Account.objects.filter(email=request.POST['email'])
        if len(user)>0:
            if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()):
                request.session['user']=user[0].id
                return redirect("/success")
            else:
                print("Wrong password!")
                messages.warning(request, 'Login failed.')
                return redirect ("/login")
        else:
            print("No such username!")
            messages.warning(request,'Login failed.')
            return redirect ("/login")
#############################register###############################
def register(request): 
    return render(request, "projapp/register.html")
#############################register_process###############################
def register_process(request):
    if request.method=="POST":
        print("-"*80)
        errors=Account.objects.register_validator(request.POST)
        if len(errors)>0:
            for tag,error in errors.items():
                messages.error(request,error, extra_tags=tag)
            return redirect("/register")
        else:
            first_name=request.POST["first_name"]
            last_name=request.POST["last_name"]
            email=request.POST["email"]
            password=bcrypt.hashpw(request.POST["password"].encode(),bcrypt.gensalt()).decode()
            print(password)
            new_user=Account.objects.create(first_name=first_name,last_name=last_name,email=email,password=password)
            request.session["user"]=new_user.id
            messages.success(request, "Successfully registered(or logged in)!")
            return redirect("/success")
#############################success###############################
def success(request):
    return render(request,"projapp/success.html")
#############################create_product###############################
def create(request):
    return redirect("/success")