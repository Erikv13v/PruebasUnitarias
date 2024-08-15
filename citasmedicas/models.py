from django.db import models

# Create your models here.

class Admin1(models.Model):
    usuario= models.CharField(max_length=100)
    correo = models.EmailField((""), max_length=254)
    contraseña = models.CharField(max_length=100)
    def __str__(self):
      return self.usuario

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveSmallIntegerField()
    correo = models.CharField(max_length=100, default=" ")
    alergia = models.CharField(max_length=100, default=" ")
    
    


class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveSmallIntegerField()
    especialidad= models.CharField(max_length=100)
   


class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    


class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    costo = models.PositiveSmallIntegerField()
