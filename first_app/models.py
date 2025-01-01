from django.db import models

# Create your models here.
class Carro(models.Model):
    title = models.TextField(max_length=200)
    year = models.TextField(max_length=4, null=True)
    color = models.TextField(max_length=200, null=True)

    def __str__(self):
        return f"{self.title} - {self.year} - {self.color}"
    
class Editor(models.Model):
    nombre = models.TextField(max_length=200)
    direccion = models.TextField(max_length=200)

    def __str__(self):
        return self.nombre
    
class Autor(models.Model):
    nombre = models.TextField(max_length=200)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.TextField(max_length=200)
    fecha_publicacion = models.DateField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    autores_atrib = models.ManyToManyField(Autor, related_name='autores')

    def __str__(self):
        return self.titulo