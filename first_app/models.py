from django.db import models

# Create your models here.
class Carro(models.Model):
    title = models.TextField(max_length=200)
    year = models.TextField(max_length=4, null=True)

    def __str__(self):
        return f"{self.title} - {self.year}"