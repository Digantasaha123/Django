# Generated by Django 5.0.6 on 2024-05-22 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vege', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipe_name', models.CharField(max_length=100)),
                ('receipe_description', models.TextField()),
                ('receipe_image', models.ImageField(upload_to='receipe')),
            ],
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]