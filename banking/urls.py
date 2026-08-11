from . import views
from django.urls import path 

app_name = "banking"

urlpatterns = [
    path("<int:bk_id>/", views.banking_detail, name = "banking_id"),
    path("<int:bk_id>/synk/", views.synkhronisation, name = "synk"),
    path("<int:bk_id>/disconnect/", views.disconnect_account, name="disconnection")
]