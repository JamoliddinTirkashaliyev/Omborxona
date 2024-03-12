from django.urls import path
from .views import *

urlpatterns = [
    path('bolimlar/', BolimlarView.as_view(), name='bolimlar'),
    path('mahsulotlar/', MahsulotlarView.as_view(), name='mahsulotlar'),
    path('mahsulotlar/<int:pk>/tahrirlash/', MahsulotTahrirlashView.as_view()),
    path('mijozlar/<int:pk>/tahrirlash/', MijozTahrirlashView.as_view()),
    path('mijozlar/', MijozlarView.as_view(), name='mijozlar'),
    path('statistika/', StatistikaView.as_view(), name='statistika'),
    path('mahsulot_ochir/<int:pk>/', MahsulotOchirishView.as_view()),
    path('mijoz_ochir/<int:pk>/', MijozOchirishView.as_view()),
]
