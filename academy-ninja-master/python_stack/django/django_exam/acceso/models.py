from django.db import models
import re


class UsuarioManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        if len(postData['nombre']) < 2:
            errors["nombre"] = "Nombre debe tener al menos dos caracteres"
        return errors
    
class regaloManager(models.Manager):
    def basic_validator(self, postData):
        errors2 = {}
        
        if len(postData['nombre']) < 2:
            errors2["nombregift"] = "Regalo debe tener al menos dos caracteres"
        return errors2
        
        
        

class Usuario(models.Model):
    nombre = models.CharField(max_length=45, unique=True, verbose_name="Nombre")
    username = models.CharField(max_length=45, unique=True, verbose_name="Username")
    email = models.EmailField(max_length=200, unique=True, verbose_name="Email")
    password = models.CharField(max_length=72)
    birthday = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsuarioManager()
    #regalos = #lista de regalos
    
class Regalo(models.Model):
    usuario = models.ForeignKey(Usuario, related_name="regalos", on_delete=models.CASCADE)
    nombregift = models.CharField(max_length=70)
    descripcion = models.CharField(max_length=30, default='vacio')
    estado = models.TextField(max_length=1, default=0)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = regaloManager()
    
    def __str__(self):
        return f"{self.id} - {self.nombregift}"
