from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import User

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

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("users:user")
    else:
        form = UserCreationForm()

    return render(request, "users/register.html", {"form": form})