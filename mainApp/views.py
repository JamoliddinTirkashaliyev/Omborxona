from django.shortcuts import render, redirect
from django.views import View
from .models import *
from statsApp.models import *
from django.db.models import Q
import datetime


class BolimlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "bo'limlar.html")
        return redirect('login')


class MahsulotlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            sotuvlar = Sotuv.objects.filter(tarqatuvchi=request.user)
            mahsulotlar = Mahsulot.objects.filter(tarqatuvchi=request.user)
            if request.GET.get('search'):
                mahsulotlar = mahsulotlar.filter(
                    Q(nom__contains=request.GET.get('search')) |
                    Q(brend__contains=request.GET['search'])
                )
            context = {
                'tarqatuvchi': request.user,
                'mahsulotlar': mahsulotlar,
                'sotuvlar': sotuvlar,
            }

            return render(request, "mahsulotlar.html", context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            Mahsulot.objects.create(
                nom=request.POST.get('nom'),
                brend=request.POST.get('brend'),
                narx1=request.POST.get('narx1'),
                narx2=request.POST.get('narx2'),
                miqdor=request.POST.get('miqdor'),
                olchov=request.POST.get('olchov'),
                sana=request.POST.get('sana'),
                tarqatuvchi=request.user
            )
            return redirect('mahsulotlar')
        return redirect('login')


class MahsulotTahrirlashView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mahsulot = Mahsulot.objects.get(id=pk)
            return render(request, "mahsulot-tahrirlash.html", {"mahsulot": mahsulot})

    def post(self, request, pk):
        if request.user.is_authenticated:
            mahsulot = Mahsulot.objects.get(id=pk)
            if mahsulot.tarqatuvchi != request.user:
                return redirect('login')
            mahsulot.nom = request.POST.get('nom')
            mahsulot.brend = request.POST.get('brend')
            mahsulot.narx1 = request.POST.get('narx1')
            mahsulot.narx2 = request.POST.get('narx2')
            mahsulot.miqdor = request.POST.get('miqdor')
            mahsulot.olchov = request.POST.get('olchov')
            mahsulot.sana = datetime.datetime.now()
            mahsulot.save()
            return redirect('mahsulotlar')
        return redirect('login')


class MahsulotOchirishView(View):
    def get(self, request, pk):
        Mahsulot.objects.get(id=pk).delete()
        return redirect("mahsulotlar")


class MijozlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            mijozlar = Mijoz.objects.filter(tarqatuvchi=request.user)
            sotuvlar = Sotuv.objects.filter(tarqatuvchi=request.user)
            if request.GET.get('search'):
                mijozlar = mijozlar.filter(
                    Q(ism__contains=request.GET.get('search')) |
                    Q(dokon__contains=request.GET['search']) |
                    Q(tel__contains=request.GET['search'])
                )
            contect = {'sotuvlar': sotuvlar,
                       'tarqatuvchi': request.user,
                       'mijozlar': mijozlar,

                       }
            return render(request, "mijozlar.html", contect)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            Mijoz.objects.create(
                ism=request.POST.get('ism'),
                dokon=request.POST.get('dokon'),
                tel=request.POST.get('tel'),
                manzil=request.POST.get('manzil'),
                tarqatuvchi=request.user
            )
            return redirect('mijozlar')
        return redirect('login')


class MijozTahrirlashView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mijoz = Mijoz.objects.get(id=pk)
            return render(request, "mijoz-tahrirlash.html", {"mijoz": mijoz})

    def post(self, request, pk):
        if request.user.is_authenticated:
            mijoz = Mijoz.objects.get(id=pk)
            if mijoz.tarqatuvchi != request.user:
                return redirect('login')
            mijoz.ism = request.POST.get('ism')
            mijoz.dokon = request.POST.get('dokon')
            mijoz.tel = request.POST.get('tel')
            mijoz.manzil = request.POST.get('manzil')

            mijoz.save()
            return redirect('mijozlar')
        return redirect('login')


class MijozOchirishView(View):
    def get(self, request, pk):
        Mijoz.objects.get(id=pk).delete()
        return redirect("mijozlar")


class StatistikaView(View):
    def get(selfr, request):
        if request.user.is_authenticated:
            return render(request, 'statistikalar.html')
        return redirect('login')
