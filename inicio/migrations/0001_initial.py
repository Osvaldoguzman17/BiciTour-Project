# Generated by Django 5.0.6 on 2024-07-06 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registroUsuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='clave')),
                ('correo', models.TextField()),
                ('nombre', models.TextField()),
                ('contraseña', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'registroUsuario',
                'verbose_name_plural': 'registroUsuarios',
                'ordering': ['-created'],
            },
        ),
    ]
