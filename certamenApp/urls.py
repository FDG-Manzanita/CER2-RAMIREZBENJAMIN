from django.urls import path
from certamenApp import views

urlpatterns = [
    path('', views.home , name="Inicio"),
    path('consulta', views.consulta, name="Consulta"),
    path('buscar/',views.buscar,name="buscar"),
]
