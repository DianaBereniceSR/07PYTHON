from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Critica,Categoria



# Create your views here.

def index(request):
	return render(request, "comentarios/index.html",{})

class registroUsuario(generic.CreateView):
	model=User
	template_name='comentarios/registro.html'
	form_class=UserCreationForm
	succes_url = "/"

class ListaCategorias(generic.ListView):
	model=Categoria
	template_name="comentarios/categorias.html"

def lista_criticas(request,id=1):
	queryset1=Categoria.objects.get(id=id)	
	queryset2=Critica.objects.all()
	contex={"categoria":queryset1,"criticas":queryset2}
	return render(request,"comentarios/lista_criticas.html",contex)

class Create(generic.CreateView):
 	template_name="comentarios/create.html"
 	model=Critica
 	fields=["user","titulo","categoria","contenido"]
 	success_url="/categorias"

class DetailTrabajo(generic.DetailView):
	template_name="comentarios/detail_critica.html"
	model=Critica