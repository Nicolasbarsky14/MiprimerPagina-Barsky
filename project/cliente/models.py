from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    
    
class Comentario(models.Model):
    cliente = models.ForeignKey('Cliente', null=True, blank=True, on_delete=models.SET_NULL, related_name='comentarios')
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField('Fecha de comentario')

    def __str__(self):
        return f'Comentario de {self.autor} en {self.fecha_comentario}'

class hola(models.Model):
    m = models.TextField()