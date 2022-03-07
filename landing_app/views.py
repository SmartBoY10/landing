from django.shortcuts import redirect, render
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import *
from .forms import *

class IndexView(View):
    def get(self, request):
        return render(request, "landing_app/index.html")


class SignUp(View):
    def get(self, request):
        return render(request, "landing_app/signup.html")


class RegisterUser(View):
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Qotaqbasss")
        return redirect("/sign-in")


class SignIn(View):
    def get(self, request):
        return render(request, "landing_app/signin.html")