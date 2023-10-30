from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.template import loader
from inicio.models import Producto
from inicio.forms import CrearProductoFormulario, BusquedaProductoFormulario

def inicio(request):    
   
    return render(request, 'inicio/inicio.html', {})

def nosotros(request):
    return render(request, 'inicio/nosotros.html')

def productos(request):    
   
    formulario = BusquedaProductoFormulario(request.GET)
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data.get('marca')
        listado_de_productos = Producto.objects.filter(marca__icontains=marca_a_buscar)
    
    formulario = BusquedaProductoFormulario()
    return render(request, 'inicio/productos.html', {'formulario': formulario, 'listado_de_productos': listado_de_productos})


def crear_producto(request):    
    
    if request.method == 'POST':
        formulario = CrearProductoFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            tipo = info_limpia.get('tipo')
            marca = info_limpia.get('marca')
            modelo = info_limpia.get('modelo')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio') 
            
    
            producto = Producto(marca=marca.lower(), descripcion=descripcion, anio=anio)
            producto.save()
            
            return redirect('/productos')
        else:
            return render(request, 'inicio/crear_producto.html', {'formulario': formulario})
        
    formulario = CrearProductoFormulario()
    return render(request, 'inicio/crear_producto.html', {'formulario': formulario})