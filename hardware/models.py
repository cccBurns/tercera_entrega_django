from django.db import models

class Video(models.Model):
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=30) 
    descripcion = models.CharField(max_length=250)   
    anio = models.IntegerField()    
    
    def __str__(self):
        return f'{self.tipo} - {self.marca} - {self.descripcion}- {self.anio}'

class Proce(models.Model):
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=30) 
    descripcion = models.CharField(max_length=250)   
    anio = models.IntegerField() 
    # marca = models.CharField(max_length=50)
    # modelo = models.CharField(max_length=30)
    # nucleos = models.IntegerField()
    # estado = models.CharField(max_length=20)
    # precio = models.IntegerField()
    # descripcion = models.TextField()

    def __str__(self):
        return f'{self.tipo} - {self.marca} - {self.descripcion}- {self.anio}'
    
# class Monitor(models.Model):
#     tipo = models.CharField(max_length=50)
#     marca = models.CharField(max_length=30) 
#     descripcion = models.CharField(max_length=250)   
#     anio = models.IntegerField() 
    # marca = models.CharField(max_length=50)
    # modelo = models.CharField(max_length=30)
    # pulgadas = models.IntegerField()
    # estado = models.CharField(max_length=20)
    # precio = models.IntegerField()
    # descripcion = models.TextField()

    # def __str__(self):
    #     return f'{self.tipo} - {self.marca} - {self.descripcion}- {self.anio}'