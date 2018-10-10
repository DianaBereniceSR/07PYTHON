from django.db import models

# Create your models here.

class clase1(models.Model):
	atributo1=models.CharField(max_length=50)
	atributo2=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.atributo1
		