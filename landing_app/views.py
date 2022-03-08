from django.shortcuts import redirect, render
from django.views.generic.base import View
from django.contrib import messages
from django.contrib.auth import login, logout

from .models import *
from .forms import *

class IndexView(View):
    def get(self, request):
        return render(request, "landing_app/index.html")


class AboutView(View):
    def get(self, request):
        return render(request, "landing_app/about.html")


class ContactView(View):
    def get(self, request):
        return render(request, "landing_app/contact.html")


class SignUp(View):
    def get(self, request):
        return render(request, "landing_app/signup.html")


class RegisterUser(View):
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You are succes signed up')
            return redirect('home')
        else:
            messages.error(request, 'Registration error')
        return render(request, "landing_app/signup.html")


class SignIn(View):
    def get(self, request):
        return render(request, "landing_app/signin.html")


class LoginUser(View):
    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        return render(request, "landing_app/signin.html")


class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('home')