from django.db import models

# Create your models here.



class Departamento(models.Model):
	nombre=models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.nombre

class Software(models.Model):
	nombre=models.CharField(max_length=100, null=True)
	funcion=models.CharField(max_length=500, null=True)
	departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE,default=1)

	def __str__(self):
		return self.nombre		

class Software_Departamento(models.Model):
	software=models.ForeignKey(Software, on_delete=models.CASCADE,default=1)
	departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE,default=1)

		