from django.urls import path
from inicio.views import inicio, productos, crear_producto, nosotros

urlpatterns = [
    path('', inicio, name='inicio'),
    path('productos/', productos, name='productos'),
    path('producto/crear/', crear_producto, name='crear_producto'),
    path('nosotros/', nosotros, name='nosotros'),    
]