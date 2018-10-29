from django.shortcuts import render
from django.views import generic
from .models import *
from .form import SoftwareForm, DepartamentoForm


# Create your views here.

class Directorio(generic.ListView):
	template_name="directorio/lista_software.html"
	model=Software

class CreateSoftware(generic.CreateView):
	template_name="directorio/create_software.html"
	form_class=SoftwareForm
	model=Software
	success_url="/"

class CreateDepartamento(generic.CreateView):
	template_name="directorio/create_departamento.html"
	form_class=DepartamentoForm
	model=Departamento
	success_url="/"

