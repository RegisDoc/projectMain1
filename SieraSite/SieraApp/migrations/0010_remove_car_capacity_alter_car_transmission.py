# Generated by Django 4.2.5 on 2023-12-04 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SieraApp', '0009_delete_cardetail_car_engine_car_include_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='capacity',
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]