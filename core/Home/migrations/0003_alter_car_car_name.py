# Generated by Django 5.0.6 on 2024-05-22 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_name',
            field=models.CharField(max_length=100),
        ),
    ]