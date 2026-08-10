from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 

# Create your views here.
def budget_page(request):
    temp = loader.get_template("budget.html")
    return HttpResponse(temp.render())

def budget_detail(request):
    temp = loader.get_template("budget_detail.html")
    return HttpResponse(temp.render())

def budget_edit(request):
    temp = loader.get_template("edit_budget.html")
    return HttpResponse(temp.render())

def delete_budget(request):
    temp = loader.get_template("delete_budget.html")
    return HttpResponse(temp.render())

def  budget_by_period(request):
    temp = loader.get_template("filter_budget.html")
    return HttpResponse(temp.render())

