from django.db import models

# Create your models here.
class Programa(models.Model):
    CATEGORIA_OPCIONES =[
        ('Cardio', 'Cardio'),
        ('Fuerza', 'Fuerza'),
        ('Movimiento', 'Movimiento'),
        ('Flexibilidad', 'Flexibilidad'),
        ]


    nombre= models.CharField(max_length=40)
    categoria = models.CharField (max_length=40, choices=CATEGORIA_OPCIONES, default='A definir manualmente.')
    duracion= models.IntegerField()
    capacidad= models.IntegerField()

    def __str__(self) -> str:
        return f'{self.nombre}, {self.categoria}'

class Instructores(models.Model):
    CATEGORIA_OPCIONES =[
        ('Cardio', 'Cardio'),
        ('Fuerza', 'Fuerza'),
        ('Movimiento', 'Movimiento'),
        ('Flexibilidad', 'Flexibilidad'),
        ]

    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    celular= models.IntegerField()
    categoria = models.CharField (max_length=40, choices= CATEGORIA_OPCIONES, default='A definir manualmente.')

    def __str__(self) -> str:
            return f'{self.nombre} {self.apellido} a cargo de {self.categoria}'


class Profesionales(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    celular= models.IntegerField()
    profesion= models.CharField(max_length=40, default= 'Indefinida')

    def __str__(self) -> str:
        return f'{self.apellido} - {self.profesion}'

class Miembros(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    celular= models.IntegerField()

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'

class Consultas(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()
    mensaje= models.CharField(max_length=200, default='Sin Datos.')
