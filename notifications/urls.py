from . import views
from django.urls import path

app_name = "notifications"

urlpatterns = [
    path("", views.notification_list, name="list"),
]