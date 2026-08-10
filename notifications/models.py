from django.db import models
from django.db.models import CASCADE
from BudgetBox import settings

# Create your models here.
class Notification (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= CASCADE)
    budget = models.ForeignKey('budgets.Budget', on_delete= CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"The budget for the {self.budget.category.cat_name} category is running out"