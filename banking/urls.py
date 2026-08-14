from . import views
from django.urls import path 

app_name = "banking"

urlpatterns = [
    path("", views.banking_detail, name = "banking_id"),
    path("synk/", views.synkhronisation, name = "synk"),
    path("disconnect/", views.disconnect_account, name="disconnection"),
    path("webhook/", views.mono_webhook, name="webhook")
]