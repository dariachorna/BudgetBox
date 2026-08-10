from django.db import models
from django.db.models import CASCADE
from BudgetBox import settings

class BankConnection(models.Model):
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)

    def __str__(self):
        return f"{self.created_at} - connect {self.name}'s account"

class BankAccount(models.Model):
    account_id = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.IntegerField()
    connection = models.ForeignKey(BankConnection, on_delete=CASCADE)

    def __str__(self):
        return f"Balance - {self.balance}{self.currency}"