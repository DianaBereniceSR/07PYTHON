from django.contrib import admin
from django.urls import path

from directorio import views
app_name="directorio"

urlpatterns = [
	path('',views.Directorio.as_view(),name="list_directorio"),
	path('create_software/',views.CreateSoftware.as_view(),name="createSoftware_view"),
	path('create_departamento/',views.CreateDepartamento.as_view(),name="createDepartamento_view")

]