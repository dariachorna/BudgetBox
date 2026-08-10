from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def banking_list (request):
    temp = loader.get_template("banking_list.html")
    return HttpResponse(temp.render())

def banking_detail (request):
    temp = loader.get_template("banking_detail.html")
    return HttpResponse(temp.render())

def synkhronisation (request):
    temp = loader.get_template("synkhronisation.html")
    return HttpResponse(temp.render())

def disconnect_account (request):
    temp = loader.get_template("disconnect_account.html")
    return HttpResponse(temp.render())