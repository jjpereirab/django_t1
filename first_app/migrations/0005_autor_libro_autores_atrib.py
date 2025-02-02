# Generated by Django 5.1.4 on 2025-01-01 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_editor_libro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=200)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='libro',
            name='autores_atrib',
            field=models.ManyToManyField(related_name='autores', to='first_app.autor'),
        ),
    ]
