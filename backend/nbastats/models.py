from django.db import models

# Create your models here.
class Plyers(models.Model):
    playerName = models.CharField(max_length=20, blank= False)
    