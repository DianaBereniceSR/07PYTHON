from django.urls import path
from mascota.api import views

app_name="api_mascota"

urlpatterns=[

	path('list_gatos/',views.ListGatoAPIView.as_view(),name="listAPIView"),
]