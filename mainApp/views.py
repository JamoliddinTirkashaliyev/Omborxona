from django.shortcuts import render, redirect
from django.views import View
from .models import *


class BolimlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "bo'limlar.html")
        return redirect('login')


class MahsulotlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            mahsulotlar = Mahsulot.objects.filter(tarqatuvchi=request.user)
            context = {
                'mahsulotlar': mahsulotlar,
            }

            return render(request, "mahsulotlar.html", context)
        return redirect('login')


class MijozlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            mijozlar = Mijoz.objects.filter(tarqatuvchi=request.user)
            contect = {
                'mijozlar': mijozlar

            }
            return render(request, "mijozlar.html",contect)
        return redirect('login')


class StatistikaView(View):
    def get(selfr,request):
        return render(request,'statistikalar.html')
