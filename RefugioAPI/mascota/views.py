from django.shortcuts import render
from django.views import generic
from .models import Gato
from .form import GatoForm

# Create your views here.

class list_Gatos(generic.ListView):
	template_name="Gato/list_gatos.html"
	model=Gato

class createGato(generic.CreateView):
	models=Gato
	template_name="Gato/create.html"
	#fields=["nombre","raza",'genero','edad']
	form_class=GatoForm
	success_url="/"	


