from django.contrib import admin
from django.urls import path

from drive import views
app_name="drive"

urlpatterns = [
	path('',views.vistaCategorias.as_view(), name="categoriasView"),
	path('trabajos/<int:id>',views.vistaTrabajos, name="trabajosView"),
	path('investigacion/<int:pk>',views.vistaInvestigacion.as_view(), name="investigacionView"),	
	path('create/',views.vistaCrearArchivo.as_view(),name="CrearViewArchivos"),
]