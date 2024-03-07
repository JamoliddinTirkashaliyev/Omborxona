from django.urls import path
from .views import *


urlpatterns = [
    path('bolimlar/', BolimlarView.as_view(), name='bolimlar'),
    path('mahsulotlar/', MahsulotlarView.as_view(), name='mahsulotlar'),
    path('mijozlar/', MijozlarView.as_view(), name='mijozlar'),
    path('statistika/', StatistikaView.as_view(), name='statistika'),
]
