# Generated by Django 5.0.6 on 2024-08-17 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rutas', '0004_alter_ruta_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ruta',
            name='Status',
        ),
        migrations.AddField(
            model_name='ruta',
            name='status',
            field=models.CharField(choices=[('activa', 'Activa'), ('finalizada', 'Finalizada')], default='activa', max_length=10),
        ),
    ]
