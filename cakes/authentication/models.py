from django.db import models

# Create your models here.

# Create your views here.
from django.contrib.auth.models import AbstractUser
class Rolechoice(models.TextChoices):
    ADMIN = 'Admin','Admin'
    USER = 'user','user'
class Profile(AbstractUser):
    role = models.CharField(max_length=20,choices=Rolechoice.choices)
    class Meta:
        verbose_name = 'Profiles'
        verbose_name_plural = 'Profiles'
    def __str__(self):
        return self.first_name
             
