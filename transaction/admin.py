from django.contrib import admin
from .models import Transaction, Category, MCCCode
# Register your models here.
admin.site.register(Transaction)
admin.site.register(Category)
admin.site.register(MCCCode)