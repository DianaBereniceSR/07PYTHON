from django.contrib import admin
from django.urls import path

from comentarios import views
from django.contrib.auth import views as auth_view



app_name="comentarios"

urlpatterns = [
    
    path('',auth_view.LoginView.as_view(template_name="comentarios/login.html"),name='login'),
    path('registro/',views.registroUsuario.as_view(),name="registro_view"),
    path('categorias/',views.ListaCategorias.as_view(),name="categorias_view"),
    path('categorias/crear/',views.Create.as_view(), name="create_view"),
    path('criticas/<int:id>',views.lista_criticas,name='criticas_view'),
    path('detail_critica/<int:pk>',views.DetailTrabajo.as_view(),name="detail_view"),
    
]
