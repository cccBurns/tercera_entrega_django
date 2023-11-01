from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from hardware.models import Video
from django.urls import reverse_lazy

class ListadoPlacaVideo(ListView):
    model = Video
    context_object_name = 'listado_de_placaVideo'
    template_name = 'hard/placavideo.html'

class CrearPlacaVideo(CreateView):
    model = Video
    template_name = 'hard/crear_placaVideo.html'
    fields = ['tipo', 'marca', 'descripcion', 'anio']
    success_url = reverse_lazy('placavideo')