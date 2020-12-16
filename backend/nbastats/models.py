from django.db import models
from django.conf import settings
import os

# Create your models here.
class Players(models.Model):
    playerID = models.IntegerField(primary_key=True)
    playerName = models.CharField(max_length= 20) 
    playerAvatar = models.ImageField(upload_to = os.path.join(settings.BASE_DIR,'static'))