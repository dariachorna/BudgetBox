
from datetime import timezone

from django.http import HttpResponse
import requests
import json
from django.shortcuts import redirect, render
from django.template import loader

from transaction.models import Category, MCCCode, Transaction
from .models import BankConnection
from django.contrib.auth.decorators import login_required
from .forms import BankConnectForm


@login_required
def banking_detail (request):
    connection = BankConnection.objects.filter(user=request.user).first()
    return render(request, "banking/banking_detail.html", {"connection": connection})

@login_required
def synkhronisation (request):
    if request.method == "POST":
        token = request.POST.get("token")
        response = requests.get("https://api.monobank.ua/personal/client-info", headers={"X-Token":token})
        if response.status_code == 200:
            data = response.json()
            acc_id = data["accounts"][0]["id"]
            BankConnection.objects.update_or_create(
                user = request.user,
                token = token,
                account_id=acc_id,
                name = "Monobank"
            )
            return redirect("banking:banking_id")
        else:
            form = BankConnectForm(request.POST)
            return render(request, "banking/synkhronisation.html", {"form":form, "error": "Failed to connect account. Check the token and try again."})

    else:
        form = BankConnectForm()
        return render(request, 'banking/synkhronisation.html', {"form":form})

@login_required
def disconnect_account (request):
    connection = BankConnection.objects.filter(user=request.user).first()
    if not connection:
        return redirect("banking:synkhronisation")

    if request.method == "POST":
        connection.delete()
        return redirect("banking:banking_id")
    return render(request, "banking/disconnect_account.html", {"disconnection": connection})

def mono_webhook (request):
    if request.method == "POST":
        data = json.loads(request.body)
        account_id = data["data"]["account"]
        amount = int(data["data"]["statementItem"]["amount"]) / 100
        mcc_code = data["data"]["statementItem"]["mcc"]
        desc = data["data"]["statementItem"]["description"]

        connection = BankConnection.objects.filter(account_id=account_id).first()
        if not connection:
            return HttpResponse(status=200)

        mcc_entry = MCCCode.objects.filter(mcc_code=mcc_code).first()
        if mcc_entry:
            category = mcc_entry.category_code
        else:
            category = Category.objects.get_or_create(cat_name="Інше")[0]

        transaction = Transaction.objects.create(user = connection.user, category = category, amount= amount, description = desc, date=timezone.now() )

        return HttpResponse(status=200)
    
    return HttpResponse(status=405)