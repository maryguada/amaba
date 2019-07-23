from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,"projapp/home.html")

def login(request): 
    return render(request, "projapp/login.html")

def register(request): 
    return render(request, "projapp/register.html")