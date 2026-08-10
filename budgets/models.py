from django.db import models
from django.db.models import CASCADE, PROTECT
from BudgetBox import settings

# Create your models here.
class Budget(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    category = models.ForeignKey('transaction.Category', on_delete=PROTECT)
    limit_amount = models.DecimalField(max_digits=12, decimal_places=2)
    month = models.DateField()

    def __str__(self):
        return f"Limin on {self.category} - {self.limit_amount} per {self.month}"