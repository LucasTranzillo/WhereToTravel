from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify

# Create your models here.

class Base(models.Model):
    create = models.DateField('data_create', auto_now_add=True)
    modified = models.DateField('data_update', auto_now=True)
    active= models.BooleanField('is_active', default=True)

    class Meta:
        abstract= True

class User(models.Model):
    name = models.CharField('name', max_length=80)
    age = models.IntegerField('age')
    username = models.CharField('user', max_length=40)

class Stories(models.Model):
    title = models.CharField('title', max_length=60)
    type = models.CharField('type', max_length=50)


class Places(models.Model):
    name = models.CharField('name', max_length=600)
    location = models.CharField('location', max_length=100)
    img = StdImageField('img', upload_to='places', variations={'thumb': (200,200)})
    slug = models.SlugField('slug', max_length=100, blank=True, editable=False)


    def __str__(self):
        return self.name

def place_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)

signals.pre_save.connect(place_pre_save, sender=Places)









