# Generated by Django 5.1.4 on 2024-12-31 22:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_carro_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=200)),
                ('direccion', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(max_length=200)),
                ('fecha_publicacion', models.DateField()),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.editor')),
            ],
        ),
    ]
