from django.urls import path
from mascota import views
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth.decorators import login_required
#from .models import Gato

app_name="mascota"

urlpatterns=[
	path('', login_required(views.list_Gatos.as_view()),name="list_view"),
	path('create/', login_required(views.createGato.as_view()),name="create_view"),
	path('accounts/login/',LoginView.as_view(template_name='Gato/login.html'),name="login_view"),
	path('logout/',logout_then_login, name='logout'),
]