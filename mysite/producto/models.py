from django.db import models

class Productos (models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    cantidad = models.CharField(max_length=5)
    
    def __str__(self):
        return self.nombre
