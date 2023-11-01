from django.urls import path
from hardware.views import ListadoPlacaVideo, CrearPlacaVideo

urlpatterns = [
    path('placavideo/' , ListadoPlacaVideo.as_view(), name='placavideo'),
    path('placavideo/crear/' , CrearPlacaVideo.as_view(), name='crear_placavideo'),
    
]
