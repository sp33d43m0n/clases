from django import forms
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.db.models import Q
from django.views import View
from acceso.forms import *
from acceso.models import * 
from django.contrib import messages
import bcrypt




def added(request,id):
    
    if request.method == 'GET':
        contexto = {
            'listaRegalos' : Regalo.objects.filter(usuario=id).filter(estado=0).order_by("-updated_at"),
            'listaRegalostodos': Regalo.objects.all().filter(estado=1),
    
            }
        return render(request, 'app/index.html', contexto)
    
def editar(request,id):      
    regalo=Regalo.objects.get(id=id)
    
    if request.method == "GET":
        contexto = {"nombre": regalo }
        return render(request, 'app/editar.html', contexto)
    
    if request.method == "POST":
        print(request.POST)
        
        iduser = request.session['usuario'] 
        id2=iduser['id']
        regalo.nombregift = request.POST['nombre']
        regalo.descripcion = request.POST['descripcion']
        regalo.save()
        
        return redirect(f"/acceso/added/{id2}")
  
    
def otorgar(request,id):
        
        iduser = request.session['usuario'] 
        id2=iduser['id']

        regaloid=Regalo.objects.get(id=id)
        regaloid.estado=1
        regaloid.save()
                        
        return redirect(f"/acceso/added/{id2}")
    
def borrar(request,id):      

        iduser = request.session['usuario'] 
        id2=iduser['id']

        regaloid=Regalo.objects.get(id=id)
        regaloid.delete()
                        
        return redirect(f"/acceso/added/{id2}")

def makeawish(request):
    if request.method == "GET":

        return render(request, 'app/wish.html')
    
    if request.method == "POST":
        print(request.POST)
        
        iduser = request.session['usuario'] 
        id2=iduser['id']
        
        nombregift = request.POST['nombre']
        descripcion = request.POST['descripcion']
        # errors2 = Regalo.objects.basic_validator(request.POST)
        # print(errors2)
        
        # if len(errors2) > 0:
        #     for valor in errors2.values():
        #         messages.errors2(request, valor)                
        # return render(request, 'app/wish.html')
        
        # else:

        usuarioid= Usuario.objects.get(id=id2)
        Regalo.objects.create(usuario=usuarioid, nombregift=nombregift, descripcion=descripcion)
        # messages.success(request, "Usuario editado con exito!!")   
            
        return redirect(f"/acceso/added/{id2}")
    
def like(request):
    pass

