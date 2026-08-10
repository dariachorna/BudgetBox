from django.contrib import admin
from .models import BankConnection, BankAccount
# Register your models here.
admin.site.register(BankConnection)
admin.site.register(BankAccount)