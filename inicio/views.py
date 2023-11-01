from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.template import loader
from inicio.models import Monitor
from inicio.forms import CrearMonitorFormulario, BusquedaMonitorFormulario

def inicio(request):    
   
    return render(request, 'inicio/inicio.html', {})

def nosotros(request):
    return render(request, 'inicio/nosotros.html')

def monitor(request):    
   
    formulario = BusquedaMonitorFormulario(request.GET)
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data.get('marca')
        listado_de_monitores = Monitor.objects.filter(marca__icontains=marca_a_buscar)
    
    formulario = BusquedaMonitorFormulario()
    return render(request, 'inicio/monitor.html', {'formulario': formulario, 'listado_de_monitores': listado_de_monitores})


def crear_monitor(request):    
    
    if request.method == 'POST':
        formulario = CrearMonitorFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            tipo = info_limpia.get('tipo')
            marca = info_limpia.get('marca')
            modelo = info_limpia.get('modelo')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio') 
            
    
            monitor = Monitor(marca=marca.lower(), descripcion=descripcion, anio=anio)
            monitor.save()
            
            return redirect('/monitor')
        else:
            return render(request, 'inicio/crear_monitor.html', {'formulario': formulario})
        
    formulario = CrearMonitorFormulario()
    return render(request, 'inicio/crear_monitor.html', {'formulario': formulario})