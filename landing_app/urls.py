from django.urls import path
from .views import *

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("sign-up/", SignUp.as_view(), name="sign_up"),
    path("register-user/", RegisterUser.as_view(), name="register_user"),
    path("sign-in/", SignIn.as_view(), name="sign_in"),
    path("login/", LoginUser.as_view(), name="login"),
]