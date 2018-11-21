from rest_framework import generics
from mascota.api.serializers import GatoModelSerializer
from mascota.models import Gato


class ListGatoAPIView(generics.ListAPIView):
	serializer_class=GatoModelSerializer

	def get_queryset(self, *args,**kwargs):
		return Gato.objects.all()

