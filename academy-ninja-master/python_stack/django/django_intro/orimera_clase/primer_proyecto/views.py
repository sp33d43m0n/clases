from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

def hola(request):
    return HttpResponse("hola como estas")

def saludar(request):
    return HttpResponse("saludos desde Col.")

def saludar_nombre(request, nombre):
    return HttpResponse(f"saludos Sr(a): {nombre}")

def aumenta(request, cantidad):
    return HttpResponse(f"aumentando en 10: { cantidad + 10 }")

def  editar(request, id):
    return HttpResponse(f"editando el id del usuario {id}")

# def template(request):
#     return render(request, 'primer_proyecto/main.html')