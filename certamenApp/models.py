from django.db import models

# Create your models here.

class Correo(models.Model):
    emisor=models.CharField(max_length=50)
    receptor=models.CharField(max_length=50)
    departamento=models.IntegerField()
    edificio=models.CharField(max_length=20,null=True)
    fecha=models.DateField(default='2022-11-13')
    entregado_pa=(
        ('Entregado','Entregado'),
        ('En Conserjeria','En Conserjeria')
        )
    Estado = models.CharField(max_length=30, choices= entregado_pa,null=True)

class Residencia(models.Model):
    NumDepEdificio=models.IntegerField()
    Edificio=models.CharField(max_length=20,null=True)
    Direccion=models.CharField(max_length=50,null=True)

