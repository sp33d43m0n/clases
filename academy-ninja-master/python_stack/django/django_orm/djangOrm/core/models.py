from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PWD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,15}$')

class UsuarioManager(models.Manager):
    def saludar(self, name=None):
            if name:
                print("HOLA A TI", name)
            return self
        
    def basic_validator(self, postData):
        errors = {}
        # agregue claves y valores al diccionario de errores para cada campo no válido
        if len(postData['nombre']) < 3:
            errors["nombre"] = "Nombre debe tener al menos 3 caracteres"
        if len(postData['apellido']) < 5:
            errors["apellido"] = "apellido no puede tener menor de 5 caracteres"
        if self.filter(email=(postData['email'])).exists(): #importante traemos self ya que estamos entregando el nombre y el object desde views 
            errors["email"] = "Tu correo ya esta registrado"
        if postData['pwd'] != postData['pwdr']:
            errors['pwd'] = "Las contraseñas no coinciden"
        if not PWD_REGEX.match(postData['pwd']):
            errors['pwd_regexpr'] = "La contraseña no es segura"  
        
        return errors
            
# Create your models here.

class Usuario(models.Model):
    
    SEXO1 = 'SH'
    SEXO2 = 'SM'
    SEXO3 = 'NB'
    SEXO4 = 'NA'
    
    TIPO_GENERO = (
        (SEXO1, 'Hombre'),
        (SEXO2, 'Mujer'),
        (SEXO3, 'No binario'),
        (SEXO4, 'Indefinido'),
        )
    
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    Genero = models.CharField(max_length=2, choices=TIPO_GENERO, default=SEXO4)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=72)
    description = models.TextField(default='')
    bithday = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsuarioManager()
    
