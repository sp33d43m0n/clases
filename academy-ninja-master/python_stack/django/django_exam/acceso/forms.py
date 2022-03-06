from ast import Gt
from django import forms
from acceso.models import *
from acceso.models import Usuario
from acceso.views import *
# from django.contrib import messages
# import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PWD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,15}$')

class UsuarioForm(forms.ModelForm):
    
    Confirmar_Password = forms.CharField(label="Confirmar password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    #validacion de contraseña
    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        if cleaned_data.get('password') != cleaned_data.get('Confirmar_Password'):
            self.add_error('Confirmar_Password', "Las contraseñas no coinciden")
            return cleaned_data
    
    class Meta:
        model = Usuario
        fields = ['nombre', 'username', 'email', 'password']
        
        labels = {
            'nombre': 'Nombre:  ',
            'username': 'Username:  ',
            'email': 'Correo  ',  
            'password': 'Contraseña  ',
            # 'birthday': 'Cumpleaños  ',
        }
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}), 
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            # 'birthday': forms.DateField(attrs={'class': 'form-control'}),   
        }
        
        
        
    #validacion de cantidad de letras en el nombre
    # def clean_nombre(self):
    #     nombre = self.cleaned_data['nombre']
    #     print(nombre)
    #     if len(nombre) < 3:
    #         self.add_error('nombre', 'Mas de dos caracteres')
    #         return nombre
        
    #contraseña segura
    # def clean_pwd(self, postData):
    #     password = self.cleaned_data['password']
    #     print(password)
    #     if not PWD_REGEX.match(password):
    #         self.add_error('password', 'La contraseña no es segura')
    #         return password