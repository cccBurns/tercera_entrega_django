from django.db import models

class Producto(models.Model):
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=100, default='TuValorModeloPredeterminado')
    descripcion = models.CharField(max_length=250)
    anio = models.IntegerField()    
    
    def __str__(self):
        return f'{self.tipo} - {self.marca} - {self.modelo} - {self.descripcion} - {self.anio}'

# class Paleta(models.Model):
#     marca = models.CharField(max_length=30)
#     descripcion = models.TextField()
#     anio = models.IntegerField()
    
#     def __str__(self):
#         return f'{self.id} - {self.marca} - {self.descripcion} - {self.anio}'
    
# class Video(models.Model):
#     marca = models.CharField(max_length=50)
#     modelo = models.CharField(max_length=30)
#     estado = models.CharField(max_length=20)
#     precio = models.IntegerField()
#     descripcion = models.TextField()
    
    # def __str__(self):
    #     return f'Id: {self.id} - Marca: {self.marca} - Modelo: {self.modelo} - Estado: {self.estado} - Precio: {self.precio} - Descripcion: {self.descripcion}'
    
# class Procesador(models.Model):
#     marca = models.CharField(max_length=50)
#     modelo = models.CharField(max_length=30)
#     nucleos = models.IntegerField()
#     estado = models.CharField(max_length=20)
#     precio = models.IntegerField()
#     descripcion = models.TextField()
    
# class Monitor(models.Model):
#     marca = models.CharField(max_length=50)
#     modelo = models.CharField(max_length=30)
#     pulgadas = models.IntegerField()
#     estado = models.CharField(max_length=20)
#     precio = models.IntegerField()
#     descripcion = models.TextField()