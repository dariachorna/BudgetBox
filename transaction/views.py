from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
transactions = [

]

def transaction_list(request):
    temp = loader.get_template("transaction_list.html")
    return HttpResponse(temp.render())

def transaction_detail(request):
    temp = loader.get_template("transaction_detail.html")
    return HttpResponse(temp.render())

def soreted_transaction(request):
    temp = loader.get_template("soreted_transaction.html")
    return HttpResponse(temp.render())

def transaction_by_category(request):
    temp = loader.get_template("transaction_by_category")
    return HttpResponse(temp.render())
