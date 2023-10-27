from django import forms

# class ProductoFormulario(forms.Form):
#     marca = forms.CharField(max_length=40)
#     modelo = forms.CharField(max_length=40)
#     estado = forms.CharField(max_length=40)
#     precio = forms.IntegerField()
#     descripcion = forms.TimeField()
    
class CrearPaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)
    anio = forms.IntegerField()
    
class BusquedaPaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)