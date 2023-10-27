from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.template import loader
from inicio.models import Video, crear_producto
from inicio.forms import CrearVideoFormulario, BusquedaVideoFormulario

def video(request):
        return render(request,"inicio/inicio.html")

def inicio(request):    
    
    return render(request, 'inicio/inicio.html', {})

def videos(request):    
    
    formulario = BusquedaVideoFormulario(request.GET)
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data.get('marca')
        listado_de_videos = video.objects.filter(marca__icontains=marca_a_buscar)
    
    formulario = BusquedaVideoFormulario()
    return render(request, 'inicio/video.html', {'formulario': formulario, 'listado_de_videos': listado_de_videos})



def crear_video(request):    
    
    if request.method == 'POST':
        formulario = CrearVideoFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            modelo = info_limpia.get('modelo')
            estado = info_limpia.get('estado')
            precio = info_limpia.get('precio')
            descripcion = info_limpia.get('descripcion')
            
    
            video = Video(marca=marca.lower(), modelo=modelo, estado=estado, precio=precio, descripcion=descripcion)
            video.save()
            
            return redirect('videos')
        else:
            return render(request, 'inicio/crear_producto.html', {'formulario': formulario})
        
    formulario = CrearVideoFormulario()
    return render(request, 'inicio/crear_producto.html', {'formulario': formulario})