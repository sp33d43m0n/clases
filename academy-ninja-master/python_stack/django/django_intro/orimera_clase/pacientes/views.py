from django.shortcuts import render, HttpResponse
# http://127.0.0.1:8000/paciente
# Create your views here.
def index(request):
    return HttpResponse('Yo soy el paciente INDEX cero')

def listado(request):
    return HttpResponse('Yo soy el listado de pacientes')

def plantillaUno(request):
    apellido = 'melendez'
    
    contexto = {'nombre' : 'javier',
                'apellido': apellido
                
                }
    return render(request, 'pacientes/main.html', contexto)
