from django.contrib.auth import authenticate, login, logout
from .models import *
from django.views import View
from django.shortcuts import render,redirect



class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user is not None:
            login(request, user)
            return redirect('bolimlar')
        return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

