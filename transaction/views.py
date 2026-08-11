from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Transaction
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from budgets.models import Budget

@login_required
def transaction_list(request):
    all_tr = Transaction.objects.filter(user=request.user)
    return render(request, 'transaction/transaction_list.html', {"transactions":all_tr})

@login_required
def transaction_detail(request, tr_id):
    transaction = get_object_or_404(Transaction, id=tr_id)
    if transaction.user != request.user:
        return HttpResponse("Access is prohibited", status=403)

    budget = Budget.objects.filter( category=transaction.category, user=request.user, month__year=transaction.date.year, month__month=transaction.date.month).first()
    total_spent = Transaction.objects.filter( category=transaction.category, user=request.user, date__year=transaction.date.year, date__month=transaction.date.month).aggregate(Sum('amount'))['amount__sum'] or 0

    remaining = budget.limit_amount - total_spent if budget else None

    return render(request, "transaction/transaction_detail.html", {
        "transaction": transaction,
        "remaining": remaining
    })

@login_required
def soreted_transaction(request):
        all_tr = Transaction.objects.filter(user=request.user).order_by('-date')
        return render(request, 'transaction/transaction_list.html', {"transactions":all_tr})


@login_required
def transaction_by_category(request, category_id):
    all_tr = Transaction.objects.filter(user=request.user, category_id=category_id)
    return render(request, 'transactions/transaction_list.html', {"transactions": all_tr})
