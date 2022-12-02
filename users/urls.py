from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("userlist/", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path(r"buy-color/<str:color>/<int:price>/", views.buy, name="buy_color"),
    path(
        r"buy-emoji/<int:emoji_id>/<int:price>/", views.buy, name="buy_emoji"
    ),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path(
        "logout/",
        LogoutView.as_view(template_name="users/logged_out.html"),
        name="logged_out",
    ),
    path(
        "login/",
        LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
]
