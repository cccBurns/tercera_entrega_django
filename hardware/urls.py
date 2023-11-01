from django.urls import path
from hardware.views import ListadoPlacaVideo, CrearPlacaVideo, ListadoProcesador, CrearProcesador

urlpatterns = [
    path('placavideo/' , ListadoPlacaVideo.as_view(), name='placavideo'),
    path('placavideo/crear/' , CrearPlacaVideo.as_view(), name='crear_placavideo'),
    path('procesador/' , ListadoProcesador.as_view(), name='procesador'),
    path('procesador/crear/' , CrearProcesador.as_view(), name='crear_procesador'),    
]

