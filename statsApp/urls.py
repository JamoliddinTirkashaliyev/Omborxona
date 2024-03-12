from django.urls import path
from .views import *



urlpatterns = [
    path('',StatistikaView.as_view(), name="statistika")

]
