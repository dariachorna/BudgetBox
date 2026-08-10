from . import views
from django.urls import path 

urlpatterns = [
    path("", views.banking_list, name="banking"),
    path("<int:id>/", views.banking_detail, name = "banking_id"),
    path("<int:id>/synk/", views.synkhronisation, name = "synk"),
    path("<int:id>/disconnect/", views.disconnect_account, name="disconnection")
]