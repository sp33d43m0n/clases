from django import forms
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from core.models import *
# from app.models import *
from datetime import datetime
from django.contrib import messages


class UsuarioForm(forms.ModelForm):
    
    # username = forms.CharField(label="Nombre de usuario")
    Confirmar_Password = forms.CharField(label="Confirmar password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    #validaciones de un campo
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        print(nombre)
        if nombre == 'JAVIER':
            self.add_error('nombre', 'No se puede usar el nombre Javier')
            return nombre
    #validacion de contraseña
    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        if cleaned_data.get('password') != cleaned_data.get('Confirmar_Password'):
            raise forms.ValidationError(
                "Las contraseñas no coinciden"
            )

        
        
    
    class Meta:
        model = Usuario
        fields = ['nombre','apellido','Genero','username','email','description','password']
    
        labels = {
            'nombre': 'nombre:  ',
            'apellido': 'apellido:  ',
            'Genero': 'genero: ',
            'username': 'nombre usuario:  ',
            'email': 'correo:  ',
            'password': 'Contraseña  ',
            'description': 'Descripcion  ',           
        }
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'Genero': forms.Select(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),  
        }
    
    # def __init__(self, *args, **kwargs):
    #     super(UsuarioForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'    
    

def add_form(request):
    if request.method == "GET":
        # contexto = { 'formModel': UsuarioForm }
        return render(request, 'core/addUserForm.html', { 'formModel': UsuarioForm })    

    if request.method == 'POST':
        print(request.POST)
        
        form = UsuarioForm(request.POST) #cargar los datos al formulario
        
        if form.is_valid():
            form.save()
            messages.success(request, 'usuario agregado correctamente')
            return redirect(reverse('core:users'))
        else:
            messages.error(request, 'con errores, solucionar')
            return render(request, 'core/addUserForm.html', { 'formModel': form })  #devolver el mismo form, para no cargar uno nuevo

def edit_form(request, id):
    if request.method == "GET":
        usuario = Usuario.objects.get(id=id)
        form = UsuarioForm(instance=usuario)
        return render(request, 'core/addUserForm.html', { 'formModel': form })
    
    if request.method == 'POST':
        print(request.POST)
        usuario = Usuario.objects.get(id=id)
        form = UsuarioForm(request.POST,instance=usuario) #cargar los datos al formulario y compararlo con lo viejo
        
        if form.is_valid():
            form.save()
            messages.success(request, 'usuario editado correctamente')
            return redirect(reverse('core:users'))
        else:
            messages.error(request, 'con errores, solucionar')
            return render(request, 'core/addUserForm.html', { 'formModel': form })
      
