import datetime

from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField('date released')
    head_img = models.ImageField(upload_to='head/%Y', blank=True, null=True)
    banner_img = models.ImageField(upload_to='banner/%Y', blank=True, null=True)
    is_banner = models.BooleanField(default=True)
    url = models.URLField(blank=True, null=True)


class News(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField('date published')
    contents = models.CharField(max_length=3000)
    url = models.URLField(blank=True, null=True)
    img = models.ImageField(upload_to="news/%Y")
