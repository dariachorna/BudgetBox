from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def users_profile(request):
    temp = loader.get_template("profile.html")
    return HttpResponse(temp.render())

def reset_password(request):
    temp = loader.get_template("password_reset.html")
    return HttpResponse(temp.render())

def verifycation(request):
    temp = loader.get_template("verify_email.html")
    return HttpResponse(temp.render())