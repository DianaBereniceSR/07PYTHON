from rest_framework import serializers
from mascota.models import Gato



class GatoModelSerializer(serializers.ModelSerializer):
	class Meta:
		model=Gato
		fields=[
			"nombre",
			"raza",
			"genero",
			"edad",
		]
