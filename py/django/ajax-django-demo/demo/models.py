from django.db import models


# Create your models here.
class Color(models.Model):
    color = models.CharField(max_length=256)


class Auto(models.Model):
    type = models.CharField('auto type', max_length=256)
    colors = models.ManyToManyField(Color)

