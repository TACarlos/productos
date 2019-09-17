from django.db import models

class Productos (models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.CharField(max_length=5, blank=True, null= True)
    cantidad = models.CharField(max_length=5)
    imagen = models.FileField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre
