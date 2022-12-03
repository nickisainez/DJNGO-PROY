from django.db import models
from datetime import datetime

class Salon(models.Model):
    aula = models.CharField(max_length=2)
    hora_entrada = models.TimeField()
    
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    idSalon = models.ForeignKey(Salon, on_delete = models.CASCADE)

    def full_name(self):
        return self.first_name + " " + self.last_name

    class Meta:
        abstract = True

class Alumno(Person):
    nota_laboratorio = models.FloatField(default=0.0)
    examen = models.FloatField(default=0.0)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['id', 'first_name', 'last_name'], name = 'primary_key_alumno'
            )
        ]

class Profesor(Person):
    salario = models.FloatField(default=0.0)
    rating = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['id', 'first_name', 'last_name'], name = 'primary_key_profesor'
            )
        ]

class Infopersona(models.Model):
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=64)

    class Meta:
        abstract = True

class Cliente(Infopersona):
    descuento = models.IntegerField()

class Vendedor(Infopersona):
    sueldo = models.IntegerField()

class Evaluacion(models.Model):
    hora_fecha = models.DateField(datetime.now())
    curso = models.CharField(max_length=200)
    evaluador = models.CharField(max_length=200)

    class Meta:
        abstract = True

class Examenfinal(Evaluacion):
    duracion_examen = models.DateField()
    n_preguntas = models.IntegerField(default=0)
    puntaje_total = models.FloatField(default=0.0)

    def puntaje_por_pregunta(self):
        return self.n_preguntas / self.puntaje_total

class Proyecto(Evaluacion):
    tema = models.CharField(max_length=100)
    n_grupos = models.IntegerField(default=0)

class ProyectoProxy(Proyecto):
    class Meta:
        proxy = True
        ordering = ['tema']

class Book(models.Model):
    title = models.CharField(max_length=400) 
    authors = models.CharField(max_length=120)
    average_rating = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    isbn13 = models.CharField(max_length=100)
    language_code = models.CharField(max_length=20)
    num_pages = models.CharField(max_length=200)
    ratings_count = models.IntegerField()
    text_reviews_count = models.IntegerField()
    publication_date = models.DateField()
    publisher = models.CharField(max_length=400)

    class Meta:
        db_table="library_books"