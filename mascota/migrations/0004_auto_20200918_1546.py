# Generated by Django 3.1.1 on 2020-09-18 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0003_contacto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota_vacuna',
            name='mascota',
        ),
        migrations.RemoveField(
            model_name='mascota_vacuna',
            name='vacuna',
        ),
        migrations.DeleteModel(
            name='supervisor',
        ),
        migrations.DeleteModel(
            name='mascota_vacuna',
        ),
        migrations.DeleteModel(
            name='vacuna',
        ),
    ]
