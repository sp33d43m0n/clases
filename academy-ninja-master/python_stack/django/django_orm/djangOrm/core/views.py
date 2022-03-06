from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from core.models import *
from app.models import *
from datetime import datetime
from django.contrib import messages

# Create your views here.


def list_users(request):
    # print(request.__dict__)
    if request.method == "GET":
        contexto = {
            'usuarios': Usuario.objects.all().order_by('id')
            }
        Usuario.objects.saludar("XAVI")
        return render(request, 'core/userList.html', contexto)
    
def add_users(request):
    if request.method == "GET":
        contexto = {"Usersinfo": Usuario.objects.all(),
            "tiposGeneros": Usuario.TIPO_GENERO}
        return render(request, 'core/addUser.html', contexto)    

    if request.method == 'POST':
        print(request.POST)
        
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        genero = request.POST['generos']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pwd']
        birthday = request.POST['cumpleanos']
        
        error= Usuario.objects.basic_validator(request.POST)
        
        # Errores renderizados sobre el mismo html
        # error_list = []
        # if len(error) > 0:
        #     for valor in error.values():
        #         error_list.append(valor)
        #     contexto = { 'errores': error_list }
        #     return render(request, 'core/addUser.html', contexto)
        
        #Presentar errores en  mensajes flash
        
        if len(error) > 0:
            for valor in error.values():
                messages.error(request, valor)                
            return render(request, 'core/addUser.html')
        
                
        else:
        
            Usuario.objects.create(nombre=nombre, apellido=apellido, Genero=genero, username=username, email=email, password=password, bithday=birthday)
            
            messages.success(request, "Usuario agregado con exito!!")
            return redirect(reverse('core:users'))

def edit_users(request, id):
    usuario=Usuario.objects.get(id=id)
    
    if request.method == "GET":
        usuario= usuario
        cumple=usuario.bithday
        cumple= cumple.strftime('%Y-%m-%d')
        contexto = {"userEdit": usuario,
                    "tiposGeneros": Usuario.TIPO_GENERO,
                    "cumple":cumple
                    }
        return render(request, 'core/editUser.html', contexto)
    
    if request.method == 'POST':
        print(request.POST)
        
        usuario.nombre = request.POST['nombre']
        usuario.apellido = request.POST['apellido']
        usuario.Genero = request.POST['generos']
        usuario.username = request.POST['username']
        usuario.email = request.POST['email']
        usuario.bithday = request.POST['cumpleanos']
        usuario.save()
        
        return redirect(reverse('core:users'))    
    
def delete_users(request, id):
    
    deluser = Usuario.objects.get(id=id)
    
    if request.method == "GET":
        contexto = {'usuario' : deluser}
        return render(request, 'core/delete.html', contexto)
    
    if request.method == 'POST':
        deluser.delete()
        contexto = { 'usuarios': Usuario.objects.all().order_by('id') }
        return render(request, 'core/userList.html', contexto) 
    
    # return redirect(reverse, ('core:users')) Preguntar porque no funciono. En la logica no deberia funcioanr
    # return render(request, 'core/userList.html', contexto)