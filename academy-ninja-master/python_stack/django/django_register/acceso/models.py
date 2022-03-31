from django.db import models
# import re
   

class Usuario(models.Model):
    nombre = models.CharField(max_length=45, unique=True, verbose_name="Nombre")
    username = models.CharField(max_length=45, unique=True, verbose_name="Username")
    email = models.EmailField(max_length=200, unique=True, verbose_name="Email")
    password = models.CharField(max_length=72)
    birthday = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  

