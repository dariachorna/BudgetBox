from django.db.models.aggregates import Sum
from django.shortcuts import redirect, render

from notifications.models import Notification
from transaction.models import Transaction
from .forms import BudgetForm
from budgets.models import Budget 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def budget_page(request):
    all_bg = Budget.objects.filter(user=request.user)
    spent_sum = []

    for budget in all_bg:
        spent = Transaction.objects.filter(user=budget.user, category= budget.category, date__year = budget.month.year, date__month = budget.month.month).aggregate(total = Sum('amount'))['total'] or 0

        if abs(spent) >= budget.limit_amount:
            status = "over"
            Notification.objects.get_or_create(user = budget.user, budget = budget)
        elif abs(spent) >= budget.limit_amount * 0.9:
            status = "warning"
            Notification.objects.get_or_create(user = budget.user, budget = budget)
        else:
            status = "ok"

        spent_sum.append({'budget':budget, 'spent':abs(spent), 'status':status})


    return render (request, "budget.html", {"budgets": spent_sum})

@login_required
def budget_detail(request, bg_id):
    budget = Budget.objects.filter(id=bg_id, user = request.user).first()
    if not budget:
        return redirect("budgets:budget")
    return render (request, "budget_detail.html", {"budget":budget})

@login_required
def budget_edit(request, bg_id):
    budget = Budget.objects.filter(id=bg_id, user = request.user).first()
    if not budget:
        return redirect("budgets:budget")
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
    budget = Budget.objects.filter(id=bg_id, user = request.user).first()
    if not budget:
        return redirect("budgets:budget")
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