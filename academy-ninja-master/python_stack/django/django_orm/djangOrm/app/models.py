from unicodedata import name
from django.db import models

# Create your models here.

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad_habitantes = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} C.H.:{self.cantidad_habitantes} MM"

class Region(models.Model):
    nombre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Movie(models.Model):
    nombre = models.CharField(max_length=50)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Wizard(models.Model):
    name = models.CharField(max_length=45)
    house = models.CharField(max_length=45)
    pet = models.CharField(max_length=45)
    year = models.IntegerField()
    
class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Camion(models.Model):
    
    SIZE_CHICO = 'C2'
    SIZE_MEDIANO = 'C4'
    SIZE_GRANDE = 'C6'
    
    TIPO_CAMION = (
        (SIZE_CHICO, 'DOS EJES'),
        (SIZE_MEDIANO, 'CUATRO EJES'),
        (SIZE_GRANDE, 'SEIS EJES'),
    )
    
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=2, choices=TIPO_CAMION, default=SIZE_CHICO)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #rutas = listade rutas del camion
    #choferes = lista de choferes
    
class Ruta(models.Model):
    camion = models.ForeignKey(Camion, related_name="rutas", on_delete=models.CASCADE)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.id} - {self.origen} - {self.destino}"
    
class Chofer(models.Model):
    camiones = models.ManyToManyField(Camion, related_name="choferes")
    nombre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.nombre}"
    
class dojos(models.Model):
    name = models.CharField(max_length=255)
    cyty = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    descr = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # ninjas = lista de ninjas asociados al dojo
    
    # def __str__(self):
    #     return f"{self.name} {self.cyty}"

class ninja(models.Model):
    dojo = models.ForeignKey(dojos, related_name="ninjas", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.id} {self.dojo} {self.first_name} {self.last_name}"
    
class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #authores = lista de autores
    def __str__(self):
        return f"{self.title} {self.desc}"

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField()
    books = models.ManyToManyField(Books, related_name="authores")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.notes}"
    
