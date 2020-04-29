# -*- coding: utf-8 -*-
from django.db import models

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
class Cars(models.Model):
    title = models.CharField(max_length=50, verbose_name='Nombre carro')
    marca_car = models.CharField(max_length=50, verbose_name='Marca carro')
    modelo_car = models.CharField(max_length=50, choices=OPCIONES_MODELO_CAR, default='sedan', verbose_name='Modelo carro')
    color_car = models.CharField(max_length=50, verbose_name='Color carro')
    patente = models.CharField(max_length=50, verbose_name='Patente', unique=True)
    num_puertas = models.IntegerField(verbose_name='Número de puertas',default='2')
    tipo_consumo = models.CharField(max_length=10, choices=OPCIONES_CONSUMO, default='bencina', verbose_name='Tipo de consumo')
    tamaño = models.CharField(max_length=15, choices=OPCIONES_TAMAÑO, default='mediano', verbose_name='Tamaño carro')
    image_car = models.ImageField(upload_to='products/', null=False, blank=False, verbose_name='Foto del carro')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.patente
    