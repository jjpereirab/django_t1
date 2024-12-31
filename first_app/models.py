from django.db import models

# Create your models here.
class Carro(models.Model):
    title = models.TextField(max_length=200)