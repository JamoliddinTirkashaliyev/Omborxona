from django.contrib import admin
from django.urls import path, include
from userApp.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('mainApp.urls')),
    path('user/', include('userApp.urls')),
    path('statistika/', include('statsApp.urls')),

    path('', LoginView.as_view(), name='login' )
]
