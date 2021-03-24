from django.db import models

class temp(models.Model):
    temp1 = models.CharField(null=True, max_length=5)
    temp2 = models.CharField(null=True, max_length=5)
    temp3 = models.CharField(null=True, max_length=5)
    temp4 = models.CharField(null=True, max_length=5)
    
class userTelegram(models.Model):
    id_telegram = models.CharField(max_length=10)
    bed = models.CharField(null=True, max_length=5)
    baby = models.CharField(null=True, max_length=5)
    pet = models.CharField(null=True, max_length=5)
    breakfast = models.CharField(null=True, max_length=5)
