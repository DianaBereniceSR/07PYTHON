from django.db import models

# Create your models here.



class autor(models.Model):
	nombreA=models.CharField(max_length=50)
	
	def __str__(self):
		return self.nombreA

class categoria(models.Model):
	categoriaM=models.CharField(max_length=30)

	def __str__(self):
		return self.categoriaM

class archivo(models.Model):
	titulo=models.CharField(max_length=100)
	categoria=models.ForeignKey(categoria, null=True, blank=True, on_delete=models.CASCADE)
	autor=models.ForeignKey(autor, null=True, blank=True, on_delete=models.CASCADE)
	timestap=models.DateTimeField(auto_now_add=True)
	contenido=models.TextField(blank=True)

	def __str__(self):
		return self.titulo






