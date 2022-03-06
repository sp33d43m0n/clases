from django import forms
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.db.models import Q
from django.views import View
from acceso.forms import *
from django.contrib import messages
import bcrypt
from acceso.models import Usuario

# Create your views here.
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


class LoginView(View):
    def get(self, request):
        
        # iduser = request.session['usuario'] 
        # id2=iduser['id']
        
        # if 'usuario' in request.session:
        #     messages.error(request, 'Ya estas logeado')
        #     return redirect(f"/acceso/added/{id2}")
            
        
        contexto = {
            'formRegister': UsuarioForm(),
            'formLogin': LoginForm(),
            
        }
        return render(request, 'acceso/login.html', contexto )
    
    def post(self, request):
        print(request.POST)
        
        form = UsuarioForm(request.POST) #cargar los datos al formulario

        
        if form.is_valid():
            usuario=form.save(commit=False)
            usuario.password =bcrypt.hashpw(usuario.password.encode(), bcrypt.gensalt()).decode()
            usuario.save()
            messages.success(request, 'usuario agregado correctamente')
            return redirect(reverse('acceso:acceso'))
        
        else:
            
            contexto = {
                'formRegister': UsuarioForm(),
                'formLogin': LoginForm(),
            }
            messages.error(request, 'con errores, solucionar')
            return render(request, 'acceso/login.html', contexto)  #devolver el mismo form, para no cargar uno nuevo
    
def login(request):
    if request.method == 'POST':
        print(request.POST)
        
        form = LoginForm(request.POST)
        
        if form.is_valid():
            
            user = Usuario.objects.filter(Q(username=form.cleaned_data['username'])| Q(email=form.cleaned_data['username'])).first()
            if user:
                form_password = form.cleaned_data['password']
                if bcrypt.checkpw(form_password.encode(), user.password.encode()):
                # si obtenemos True después de validar la contraseña, podemos poner la identificación del usuario en la sesión
                    messages.success(request, 'Bienvenido')
                    request.session['usuario'] = { 'nombre' : user.nombre, 'username' : user.username, 'email' : user.email, 'id' : user.id}
                    iduser = request.session['usuario'] 
                    id2=iduser['id']
                    return redirect(f"/acceso/added/{id2}")
                else:
                    messages.error(request, 'Contraseña o username incorrecto')
            else:
                messages.error(request, 'Contraseña o username incorrecto')
                
            return redirect(reverse('acceso:acceso'))
        else:
            
            contexto = {
                'formRegister': UsuarioForm(),
                'formLogin': form,
            }
            return render(request, 'acceso/login.html', contexto) 

def logout(request):
    
    if 'usuario' in request.session:
        messages.success(request, 'Vuelve pronto')
        del request.session['usuario']
    else:
        messages.error(request, 'No estas logeado')
    return redirect(reverse('acceso:acceso'))
    
