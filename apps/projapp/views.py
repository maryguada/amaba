from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
import bcrypt
from .models import *
#############################home###############################
def index(request):
    return render(request,"projapp/home.html")
<<<<<<< HEAD

#############################login###############################
def login(request): 
    return render(request, "projapp/login.html")

=======
#############################login###############################
def login(request): 
    return render(request, "projapp/login.html")
>>>>>>> c2b9c6ca0df6769dc7cd7d8989dc59ab4d57d293
#############################logout###############################
def logout(request):
    del request.session['user']
    return redirect("/")
<<<<<<< HEAD

=======
>>>>>>> c2b9c6ca0df6769dc7cd7d8989dc59ab4d57d293
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
<<<<<<< HEAD

#############################register###############################
def register(request): 
    return render(request, "projapp/register.html")

#############################register_process######################
=======
#############################register###############################
def register(request): 
    return render(request, "projapp/register.html")
#############################register_process###############################
>>>>>>> c2b9c6ca0df6769dc7cd7d8989dc59ab4d57d293
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
<<<<<<< HEAD

#############################success###############################
def success(request):
    return render(request,"projapp/success.html")

#############################create_product#######################
def create(request):
    return render(request,"create.html")

############################men_shirt#######################
def men_shirt(request): 
    return render(request, "projapp/men-shirt.html")

######################### women_vneck ###########
def women_vneck(request): 
    return render(request, "projapp/women-vneck.html")

######################### women_tshirt ##########
def women_tshirt(request): 
    return render(request, "projapp/women-tshirt.html")

######################### sunglass ##############
def sunglass(request): 
    return render(request, "projapp/sunglass.html")

######################## backpack #############
def backpack(request): 
    return render(request, "projapp/backpack.html")

######################## backpack #############
def jacket(request): 
    return render(request, "projapp/jeanjacket.html")

######################## boots ########


 
=======
#############################success###############################
def success(request):
    return render(request,"projapp/success.html")
#############################create_product###############################
def create(request):
    return redirect("/success")
>>>>>>> c2b9c6ca0df6769dc7cd7d8989dc59ab4d57d293
