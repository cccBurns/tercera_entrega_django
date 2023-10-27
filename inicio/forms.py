# from django import forms
# from .models import Category, Product, Customer

# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = '__all__'

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'

# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = '__all__'
        
from django import forms

class CrearPaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)
    anio = forms.IntegerField()
    
class BusquedaPaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)