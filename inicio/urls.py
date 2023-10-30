from django.urls import path
from inicio.views import inicio, productos, crear_paleta, nosotros

urlpatterns = [
    path('', inicio, name='inicio'),
    path('productos/', productos, name='productos'),
    path('paletas/crear/', crear_paleta, name='crear_paleta'),
    path('nosotros/', nosotros, name='nosotros'),    
]