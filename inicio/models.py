# from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=100)

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

# class Customer(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
    
from django.db import models

class Paleta(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = models.TextField()
    anio = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.descripcion} - {self.anio}'