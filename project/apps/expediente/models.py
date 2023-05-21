from django.db import models
from datetime import date
# Create your models here.

class Juzgado(models.Model):
    opciones_de_juzgado = (
        'Juzgado nro. 1'
        'Juzgado nro. 2'
        'Juzgado nro. 3'
        'Juzgado nro. 4'
        'Juzgado nro. 5'
        'Juzgado nro. 6'
        'Juzgado nro. 7'
        'Juzgado nro. 8'
        'Juzgado nro. 9'
        'Juzgado nro. 10'
        'Juzgado nro. 11'
        'Juzgado nro. 12')
    nombre = models.CharField(max_length=50, choices=opciones_de_juzgado)
    def __str__(self):
        return self.nombre
    
class Expediente(models.Model):
    numero_expediente = models.CharField(max_length=50, editable=False)
    anio = models.IntegerField(max_length=4, editable=False)
    caratula = models.CharField(max_length=50)
    Juzgado = models.ForeignKey(Juzgado)
