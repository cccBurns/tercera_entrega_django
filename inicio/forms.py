from django import forms
    
class CrearMonitorFormulario(forms.Form):
    tipo = forms.CharField(max_length=50)
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=250)
    anio = forms.IntegerField()
    
class BusquedaMonitorFormulario(forms.Form):
    tipo = forms.CharField(max_length=50, required=False)
    marca = forms.CharField(max_length=30, required=False)
    modelo = forms.CharField(max_length=40, required=False)
    
