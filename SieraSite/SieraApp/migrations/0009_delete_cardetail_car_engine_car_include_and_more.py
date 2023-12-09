# Generated by Django 4.2.5 on 2023-12-04 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SieraApp', '0008_remove_cardetail_location_alter_cardetail_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='carDetail',
        ),
        migrations.AddField(
            model_name='car',
            name='engine',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='include',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='transmission',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='year',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True),
        ),
    ]
