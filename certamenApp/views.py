from django.shortcuts import HttpResponse, render
from certamenApp.models import Correo
# Create your views here.

def home(request):
    return render(request, "certamenApp/home.html")

def consulta(request):
    return render(request, "certamenApp/consulta.html")

def buscar(request):
    if request.GET["cro"]:
        mensaje="Correo Buscado: %r" %request.GET["cro"]
        correoB=request.GET["cro"]

        a=Correo.objects.filter(edificio__icontains=correoB)
        return render(request,"certamenApp/resultado_busqueda.html",{"Correos":a,"query":correoB})
    else:
        mensaje="No has Introducido nada"
    return HttpResponse(mensaje)
