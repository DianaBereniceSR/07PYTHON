from django.db import models

# Create your models here.

class Gato(models.Model):
	nombre=models.CharField(max_length=50)
	raza=models.CharField(max_length=50)
	genero=models.CharField(max_length=50)
	edad=models.CharField(max_length=50)
	timestap=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nombre


