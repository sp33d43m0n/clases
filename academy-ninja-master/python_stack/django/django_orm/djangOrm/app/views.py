from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def index(request):
    # return HttpResponse("this is the equivalent of @app.route('/')")
    return render (request, "app/main.html")

def camion(request, id):
    if request.method == "GET":
        context = {"camion_info": Camion.objects.get(id=id)}
        return render (request, "app/camion.html", context) 

def camiones(request):
    
    if request.method == "GET":
        context = {"camiones_info": Camion.objects.all().order_by("-updated_at"),
                "tiposCamiones": Camion.TIPO_CAMION}
        return render (request, "app/camiones.html", context) 
    
    if request.method == "POST":
        print(request.POST)
        
        nombre = request.POST['nombre']
        tipos = request.POST['tipos']
        
        Camion.objects.create(nombre=nombre, tipo=tipos)
        
        return redirect ("/camiones")

def rutas(request):
    
    if request.method == "GET":
        context = {"rutas_info": Ruta.objects.all()}
        return render (request, "app/rutas.html", context) 
    

def chofer(request, id):
    if request.method == "GET":
        context = {"chofer_info": Chofer.objects.get(id=id),
                "Camiones": Camion.objects.exclude(choferes= Chofer.objects.get(id=id)).order_by("nombre")}
        return render (request, "app/chofer.html", context) 

def choferes(request):
    
    if request.method == "GET":
        context = {"choferes_info": Chofer.objects.all().order_by("-updated_at")}
        # flash('Esto es una prueba','error')
        return render (request, "app/choferes.html", context) 
    
    if request.method == "POST":
        print(request.POST)
        
        nombre = request.POST['nombre']
        
        Chofer.objects.create(nombre=nombre)
        
        return redirect ("/choferes")
    
def chofer_add_camion(request, id):
    print(request.POST)
    
    chofer = Chofer.objects.get(id=id)
    camion = Camion.objects.get(id=request.POST['tipos'])
    
    chofer.camiones.add(camion)
    
    return redirect(f"/chofer/{id}")

def chofer_remove_camion(request, id1, id2):
    print(request.POST)
    
    chofer = Chofer.objects.get(id=id1)
    camion = Camion.objects.get(id=id2)
    
    chofer.camiones.remove(camion)
    
    return redirect(f"/chofer/{id1}")
    

def process1(request):
    context = {
        "all_the_users": Users.objects.all(),
                
    } 
    print(context)
    return render(request, "app/index.html", context)
    # return HttpResponse("this is the equivalent of @app.route('/')!")

def process2(request):
    context = {
        "all_the_users": Users.objects.all().order_by("first_name"),                
    } 
    print(context)
    return render(request, "app/index.html", context)