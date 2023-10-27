from django.urls import path
from inicio.views import inicio, video, crear_producto
from inicio import views

urlpatterns = [
    path('', inicio, name='inicio'),
    path('video/', video, name='video'),
    path('video/crear/', crear_producto, name='crear_producto'),
    path('video', views.video,name='video'),   
]