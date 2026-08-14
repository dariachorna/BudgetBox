from django.shortcuts import redirect, render
from .forms import BudgetForm
from budgets.models import Budget 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def budget_page(request):
    all_bg = Budget.objects.all()
    return render (request, "budget.html", {"budgets": all_bg})

@login_required
def budget_detail(request, bg_id):
    budget = Budget.objects.get(id=bg_id)
    return render (request, "budget_detail.html", {"budget":budget})

@login_required
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

@login_required
def delete_budget(request, bg_id):
    budget = Budget.objects.get(id=bg_id)
    if request.method == "POST":
        budget.delete()
        return redirect("budgets:budget")
    return render(request, "delete_budget.html", {"budgets":budget})

@login_required
def create_budget(request):
    if request.method=="POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit = False)
            budget.user = request.user
            budget.save()
            return redirect("budgets:budget_detail", bg_id=budget.id)
    else: 
        form = BudgetForm()
    return render (request, "budgets/create_budget.html", {"form":form})