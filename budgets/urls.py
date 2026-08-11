from . import views
from django.urls import path

app_name = "budgets"

urlpatterns = [
    path("", views.budget_page, name = "budget"),
    path("<int:bg_id>/", views.budget_detail, name = "budget_detail"),
    path("<int:bg_id>/edit/", views.budget_edit, name = "edit_budget"),
    path("<int:bg_id>/delete/", views.delete_budget, name = "delete_budget"),
]