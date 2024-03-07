from django.db import models

from django.contrib.auth.models import AbstractUser

class Tarqatuvchi(AbstractUser):
    bolim = models.CharField(max_length=250, blank=True,null=True)
    tel = models.CharField(max_length=14, blank=True,null=True)
    manzil = models.TextField( blank=True,null=True)

    class Meta:
        verbose_name = 'Tarqatuvchi'
        verbose_name_plural = 'Tarqatuvchilar'

    def __str__(self):
        return f"{self.username} - {self.bolim}"
