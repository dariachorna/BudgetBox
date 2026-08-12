from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
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
        form=BankConnectForm(request.POST)
        if form.is_valid():
            token_value=form.cleaned_data['token']
            BankConnection.objects.create(user=request.user, token=token_value, name="/")
            return redirect("banking:banking_id")
    else:
        form = BankConnectForm()
    return render(request, "banking/synkhronisation.html", {"form":form})

@login_required
def disconnect_account (request):
    connection = BankConnectForm.objects.get(id=id)
    if request.method == "POST":
        connection.delete()
        return redirect("users/register")
    return render(request, "banking/disconnect_account.html", {"disconnection": connection})
