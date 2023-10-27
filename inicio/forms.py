from django import forms

# class ProductoFormulario(forms.Form):
#     marca = forms.CharField(max_length=40)
#     modelo = forms.CharField(max_length=40)
#     estado = forms.CharField(max_length=40)
#     precio = forms.IntegerField()
#     descripcion = forms.TimeField()
    

class CrearVideoFormulario(forms.Form):
    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)
    estado = forms.CharField(max_length=40)
    precio = forms.IntegerField()
    descripcion = forms.TimeField()
    
class BusquedaVideoFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)