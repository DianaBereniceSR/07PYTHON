from django.urls import path
from mascota import views
#from .models import Gato

app_name="mascota"

urlpatterns=[
	path('',views.list_Gatos.as_view(),name="list_view"),
	path('create/',views.createGato.as_view(),name="create_view"),
]