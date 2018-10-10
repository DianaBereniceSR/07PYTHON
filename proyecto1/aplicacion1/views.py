from django.shortcuts import render
from .models import clase1

# Create your views here. Este views esta en la carpeta aplicacion1

def metodo1(request):
	contex={"valor1":"valorsito1", "objeto1":clase1.objects.get(id=1)}
	return render(request, "carpetahtmls/index.html", contex)
