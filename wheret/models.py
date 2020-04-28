from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField('name', max_length=80)
    age = models.IntegerField('age')
    username = models.CharField('user', max_length=40)

class Places(models.Model):
    name = models.CharField('name', max_length=600)
    location = models.CharField('location', max_length=100)

class Stories(models.Model):
    title = models.CharField('title', max_length=60)
    type = models.CharField('type', max_length=50)

