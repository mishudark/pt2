from django.db import models

# Create your models here.

class data (models.Model):
    grados = models.IntegerField(max_length=2,default=0)
    humedad = models.IntegerField(max_length=3,default=0)
    viento = models.IntegerField(max_length=3,default=0)
    dir_viento = models.CharField(max_length=15)




