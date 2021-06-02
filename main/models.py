from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# from django.contrib.auth.models import AbstractUser

UserModel = get_user_model()


class UserTelegram(models.Model):
    id_telegram = models.CharField(max_length=10, primary_key=True)
    lan = models.CharField(max_length=2, null=True)
    username = models.CharField(max_length=30, null=True)
    bed = models.CharField(null=True, max_length=5)
    baby = models.CharField(null=True, max_length=5)
    pet = models.CharField(null=True, max_length=5)
    breakfast = models.CharField(null=True, max_length=5)


class Client(models.Model):
    STATE_FULLNAME = 0
    STATE_PHONE = 1
    STATE_EMAIL = 2
    STATE_IS_FIRM = 3
    STATE_COUNTRY = 4

    telegram_user_id = models.BigAutoField(primary_key=True)
    user_info = models.ForeignKey(UserTelegram, on_delete=models.CASCADE,  default=None, null=True)
    fullName = models.CharField(max_length=50, default=None, null=True)
    phone = models.CharField(max_length=15, default=None, null=True)
    email = models.CharField(max_length=50, default=None, null=True)
    is_firm = models.SmallIntegerField(default=None, null=True)
    country = models.CharField(max_length=20, default=None, null=True)
    state = models.IntegerField(default=STATE_FULLNAME)

    def __str__(self):
        return f'{self.fullName}\n{self.phone}\n{self.country} {self.user_info.lan}'
