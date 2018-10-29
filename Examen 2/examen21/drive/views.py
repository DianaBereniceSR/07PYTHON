from django.shortcuts import render
from .models import categoria,archivo
from django.views import generic

# Create your views here.

class vistaCategorias(generic.ListView):
	template_name="driveUrls/menuCategorias.html"
	model=categoria

def vistaTrabajos(request,id=1):
	categoriaT=categoria.objects.get(id=id)	
	archivos=archivo.objects.all()
	contex={"categoriaid":categoriaT,"archivosid":archivos}
	return render(request,"driveUrls/trabajos.html",contex)

class vistaInvestigacion(generic.DetailView):
	template_name="driveUrls/investigacion.html"
	model=archivo

class vistaCrearArchivo(generic.CreateView):
	template_name='driveUrls/create.html'
	model=archivo
	fields=["titulo","autor","categoria","contenido"]
	success_url="/"






