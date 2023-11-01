from django.urls import path
from inicio.views import inicio, monitor, crear_monitor, nosotros

urlpatterns = [
    path('', inicio, name='inicio'),
    path('monitor/', monitor, name='monitor'),
    path('monitor/crear/', crear_monitor, name='crear_monitor'),
    path('nosotros/', nosotros, name='nosotros'),    
]