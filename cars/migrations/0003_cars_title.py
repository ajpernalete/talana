# Generated by Django 3.0.5 on 2020-04-29 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20200429_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='Nombre carro'),
            preserve_default=False,
        ),
    ]
