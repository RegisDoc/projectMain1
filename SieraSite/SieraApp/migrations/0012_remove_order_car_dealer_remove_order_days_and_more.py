# Generated by Django 4.2.5 on 2023-12-15 14:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SieraApp', '0011_carrental'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='car_dealer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='days',
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_complete',
        ),
        migrations.RemoveField(
            model_name='order',
            name='rent',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='drop_day',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='drop_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='fullname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)]),
        ),
        migrations.AddField(
            model_name='order',
            name='pick_day',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='pick_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
