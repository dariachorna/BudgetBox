from django.db import models
from django.db.models import CASCADE, PROTECT

from BudgetBox import settings

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return f"category {self.cat_name}"

class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= CASCADE)
    category = models.ForeignKey(Category, on_delete=PROTECT)
    description = models.CharField(max_length= 350)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.date}: debited {self.amount} for {self.category} ({self.description})"
