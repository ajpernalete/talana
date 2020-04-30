# -*- coding: utf-8 -*-
import uuid

from django.db import models

from django.utils.text import slugify

from django.db.models.signals import pre_save

OPCIONES_CONSUMO = (
    ('bencina','BENCINA'),
    ('petrolero', 'PETROLERO'),
)
OPCIONES_MODELO_CAR = (
    ('microauto','MICROAUTO'),
    ('sedan','SEDAN'),
    ('suv','SUV'),
    ('todoterreno','TODOTERRENO'),
    ('coupe','COUPE'),
)
OPCIONES_TAMAÑO = (
    ('pequeño','PEQUEÑO'),
    ('mediano','MEDIANO'),
    ('grande','GRANDE'),
    ('extragrande','EXTRAGRANDE'),
)

# Create your models here.
class Car(models.Model):
    title = models.CharField(max_length=50, verbose_name='Nombre carro')
    marca_car = models.CharField(max_length=50, verbose_name='Marca carro')
    modelo_car = models.CharField(max_length=50, choices=OPCIONES_MODELO_CAR, default='sedan', verbose_name='Modelo carro')
    color_car = models.CharField(max_length=50, verbose_name='Color carro')
    patente = models.CharField(max_length=50, verbose_name='Patente', unique=True)
    num_puertas = models.IntegerField(verbose_name='Número de puertas',default='2')
    tipo_consumo = models.CharField(max_length=10, choices=OPCIONES_CONSUMO, default='bencina', verbose_name='Tipo de consumo')
    tamaño = models.CharField(max_length=15, choices=OPCIONES_TAMAÑO, default='mediano', verbose_name='Tamaño carro')
    image_car = models.ImageField(upload_to='cars/', null=False, blank=False, verbose_name='Foto del carro')
    slug = models.SlugField(null=False,blank=False,unique=True )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.patente
    
def set_slug(sender,instance, *args, **kwargs): #callback
   if instance.title and not instance.slug:
      slug = slugify(instance.title)

      while Car.objects.filter(slug=slug).exists():
         slug = slugify(
            '{}-{}'.format(instance.title, str(uuid.uuid4())[:8] )
         )

      instance.slug = slug
   

pre_save.connect(set_slug, sender=Car)