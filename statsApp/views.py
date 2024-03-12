from django.shortcuts import render, redirect
from django.views import View
from .models import *
from mainApp.models import *


class StatistikaView(View):
    def get(self, request):
        if request.user.is_authenticated:
            sotuvlar = Sotuv.objects.filter(tarqatuvchi=request.user)
            mahsulotlar = Mahsulot.objects.filter(tarqatuvchi=request.user)
            mijozlar = Mijoz.objects.filter(tarqatuvchi=request.user)
            context = {
                'sotuvlar': sotuvlar,
                'mahsulotlar': mahsulotlar,
                'mijozlar': mijozlar,
                'tarqatuvchi': request.user
            }
            return render(request, 'statistikalar.html', context)

    def post(self, request):
        if request.user.is_authenticated:
            mijoz = Mijoz.objects.get(id=request.POST.get('mijoz'))
            Sotuv.objects.create(
                mahsulot=Mahsulot.objects.get(id=request.POST.get('mahsulot')),
                mijoz=mijoz,
                sana=request.POST.get('sana'),
                miqdor=request.POST.get('miqdor'),
                summa=request.POST.get('summa'),
                tolandi=request.POST.get('tolandi'),
                qarz=request.POST.get('qarz'),
                tarqatuvchi=request.user
            )
            mijoz.qarz = sum(Sotuv.objects.filter(tarqatuvchi=request.user, mijoz__id=mijoz.id).values_list('qarz', flat=True))
            mijoz.save()
            return redirect('statistika')
        return redirect('login')
