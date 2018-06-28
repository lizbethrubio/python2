from django.db import models

# Create your models here.
class Doctor(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False, verbose_name='Nombre')
    rut = models.CharField(max_length=10, unique=True, verbose_name='RUT')
    direccion = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(auto_now_add=False, auto_now=False, verbose_name='Fecha de Nacimiento')
    fecha_ingreso_clinica = models.DateField(auto_now_add=True, verbose_name='Fecha de ingreso a la clínica')
    edad = models.PositiveSmallIntegerField(verbose_name='Edad del doctor')

    objects = models.Manager

    def __str__(self):
        return self.nombre

