from django.contrib import messages
from ast import Gt
from django import forms
from acceso.models import *
from acceso.models import Usuario
from acceso.views import *
import re



# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UsuarioForm(forms.ModelForm):
    
    
    #validacion de contraseña
    Confirmar_Password = forms.CharField(label="Confirmar password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    def clean(self):
        # errors = {}
        #cleaned_data = super().clean()
        super().clean()
        #si se genera el error de validación, el formulario mostrará un mensaje de error en la parte superior del formulario
        #print(f'*'*10,cleaned_data)
        print(self.cleaned_data.get('nombre'))
        if self.cleaned_data.get('password') != self.cleaned_data.get('Confirmar_Password'):
        #     errors["pwd_check"] = "Las contraseñas no coinciden"
        
        # return errors
            self.add_error('Confirmar_Password', "Las contraseñas no coinciden") #add_Error This method allows adding errors to specific fields from within the Form.clean() method
            # raise forms.ValidationError("Las contraseñas no coinciden")
        return self.cleaned_data
    
        #validacion de cantidad de letras en el nombre
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        print(f"C_Nombre:{nombre}")
        if len(nombre) < 3:
            self.add_error('nombre', 'Mas de dos caracteres')
        return nombre  
    
        #contraseña segura
    def clean_password(self):
        PWD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,15}$')
        #PWD_REGEX = re.compile(r'^[a-zA-Z. ]+$')
        password = self.cleaned_data['password']
        print('*'*20,'este es el',password)
        if not PWD_REGEX.match(password):
            self.add_error('password', 'La contraseña no es segura')
        return password
        
    # def clean_pwd(self):
    #     cleaned_data = super().clean() 
    #     password = cleaned_data.get['password']
    #     print(password)
    #     if not PWD_REGEX.match(password):
    #         self.add_error('password', 'La contraseña no es segura')
    #         return password
        
    
    

    

    
    class Meta:
        model = Usuario    #Usuario es la clase creada en la BD
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
        
class LoginForm(forms.Form):
    username = forms.CharField(
                label='username', 
                max_length=45, 
                required=True, 
                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Usuario o Email'})
            )
    password = forms.CharField(
                label='Contraseña', 
                required=True, 
                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'contraseña'})
            )    
        

        
