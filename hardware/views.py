from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from hardware.models import Video, Proce
from django.urls import reverse_lazy
# from inicio.forms import CrearVideoFormulario, BusquedaProceFormulario

class ListadoPlacaVideo(ListView):
    model = Video
    context_object_name = 'listado_de_placaVideo'
    template_name = 'hard/placavideo.html'

class CrearPlacaVideo(CreateView):
    model = Video
    template_name = 'hard/crear_placaVideo.html'
    fields = ['tipo', 'marca', 'descripcion', 'anio']
    success_url = reverse_lazy('placavideo')
    
class ListadoProcesador(ListView):
    model = Proce
    context_object_name = 'listado_de_procesador'
    template_name = 'hard/procesador.html'

class CrearProcesador(CreateView):
    model = Proce
    template_name = 'hard/crear_procesador.html'
    fields = ['tipo', 'marca', 'descripcion', 'anio']
    success_url = reverse_lazy('procesador')