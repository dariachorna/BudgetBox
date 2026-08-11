from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .forms import BudgetForm
from budgets.models import Budget 

# Create your views here.
def budget_page(request):
    all_bg = Budget.objects.all()
    return render (request, "budget.html", {"budgets": all_bg})

def budget_detail(request, bg_id):
    budget = Budget.objects.get(id=bg_id)
    return render (request, "budget_detail.html", {"budget":budget})

def budget_edit(request, bg_id):
    budget = Budget.objects.get(id=bg_id)
    if request.method == "POST":
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            return redirect("budgets:budget_detail", bg_id=budget.id)
        else:
            form = BudgetForm(instance=budget)

    return render(request, "edit_budget.html", {"form":form})

def delete_budget(request, bg_id):
    budget = Budget.objects.get(id=bg_id)
    if request.method == "POST":
        budget.delete()
        return redirect("budgets:budget")
    return render(request, "delete_budget.html", {"budgets":budget})
