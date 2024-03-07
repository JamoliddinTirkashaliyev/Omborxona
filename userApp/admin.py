from django.contrib import admin

from django.contrib.auth.admin import Group, UserAdmin
from .models import *


class TarqatuvchiAdmin(UserAdmin):
    fieldsets = (
        (None,{"fields":("username","password")}),
        ("Info",{"fields":("first_name","last_name","bolim","tel","manzil")}),
    )
    list_display = ('username', 'bolim', 'tel')

admin.site.unregister(Group)
admin.site.register(Tarqatuvchi,TarqatuvchiAdmin)
