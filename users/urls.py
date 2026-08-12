from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path("", views.users_profile, name="user"),
    path("password-reset/<uidb64>/<token>/", views.reset_password, name="reset_password"),
    path("verify-email/<uidb64>/<token>/", views.verifycation, name="veryfication"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register")

]