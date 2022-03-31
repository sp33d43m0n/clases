from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.db.models import Q
from django.views import View
# from acceso.forms import *
from django.contrib import messages
import bcrypt
from acceso.forms import UsuarioForm
from django.contrib.auth import authenticate, login as dj_login
from .forms import LoginForm, Usuario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout


# from acceso.models import UsuarioManager

# Create your views here.

# def indexcore(request):
#     return HttpResponse("this is the equivalent of @acceso.route('/')!")

def login_admin(request):
    # if request.method == "GET":
    #     return render(request, 'acceso/login.html')
    
    if request.method == "POST":
        print(request.POST)
        #form = AuthenticationForm(request, data=request.POST)
        # if form.is_valid():
        username = request.POST['nombre_admin']
        password = request.POST['pwd_admin']
        
        user = authenticate(username=username, password=password)
        if user is not None :
                dj_login(request, user)
                messages.info(request, f"Estas logeado dentro de admin {username}.")
                print("LOGIN!")
                return render(request, 'acceso/pageadmin.html', context={} )
        else:
            print("NO LOGIN!")
            messages.error(request,"Usuario o password invalido")
            form = UsuarioForm()
            return redirect(reverse('acceso:acceso'))
        # else:
            #print("NO VALIDO!")
            # messages.error(request,"Usuario o password invalido")
        # form = AuthenticationForm()
        # return render(request=request, template_name="acceso/register.html", context={"login_form":form})
    
            # form = UsuarioForm()
            # return render(request,"acceso/register.html", context={"form_Register":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out")
    contexto = {
        'formRegister': UsuarioForm(),        
    }
    return render(request, 'acceso/register.html', contexto )
    


#clase para registro
class LoginView(View): 
    def get(self, request):
        
        # iduser = request.session['usuario'] 
        # id2=iduser['id']
        
        # if 'usuario' in request.session:
        #     messages.error(request, 'Ya estas logeado')
        #     return redirect(f"/acceso/added/{id2}")
            
        
        contexto = {
            'formRegister': UsuarioForm(),
            # 'formLogin': LoginForm(),
            
        }
        return render(request, 'acceso/register.html', contexto )
    
    def post(self, request):
        print(request.POST)
        
        form = UsuarioForm(request.POST) #cargar los datos al formulario
        # print(form)

        
        if form.is_valid():
            usuario=form.save(commit=False) #commit=false no se guarda en la Bds
            usuario.password =bcrypt.hashpw(usuario.password.encode(), bcrypt.gensalt()).decode()
            usuario.save()
            messages.success(request, 'usuario agregado correctamente')
            return redirect(reverse('acceso:loginlocalbd'))
        
        else:
            
            contexto = {
                'formRegister': form,
                # 'formLogin': LoginForm(),
            }
            print('*'*20,contexto)
            messages.error(request, 'con errores, solucionar')
            return render(request, 'acceso/login.html', contexto)  #devolver el mismo form, para no cargar uno nuevo
        
def loginbdlocal(request):
    if request.method == "GET":
        
        contexto = {
        # 'formRegister': UsuarioForm(),
            'formLogin': LoginForm(),
            }
        return render(request, 'acceso/login.html', contexto )
        
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
                    # idname=iduser['nombre']
                    return redirect(reverse('acceso:logeduser'))
                    # return redirect(f"/acceso/added/{idname}")
                else:
                    messages.error(request, 'Contraseña o username incorrecto')
            else:
                messages.error(request, 'Contraseña o username incorrecto')
                
            return redirect(reverse('acceso:loginlocalbd'))
        # else:
            
        #     contexto = {
        #         # 'formRegister': UsuarioForm(),
        #         'formLogin': form,
        #     }
        #     return render(request, 'acceso/login.html', contexto) 

def logedadmin(request):
    contexto={}
    return render(request, 'acceso/pageadmin.html', contexto)

def logeduser(request):
    contexto={}
    return render(request, 'acceso/page.html', contexto)

def active(request):
    contexto={}
    return render(request, 'acceso/testurl.html', contexto)

def link1(request):
    contexto={}
    return render(request, 'acceso/testurl.html', contexto)

def link2(request):
    contexto={}
    return render(request, 'acceso/testurl.html', contexto)

    # return render(request, 'acceso/login.html', context={"login_form":form} )
# def login(request):
#     if request.method == 'POST':
#         print(request.POST)
        
#         form = LoginForm(request.POST)
        
#         if form.is_valid():
            
#             user = Usuario.objects.filter(Q(username=form.cleaned_data['username'])| Q(email=form.cleaned_data['username'])).first()
#             if user:
#                 form_password = form.cleaned_data['password']
#                 if bcrypt.checkpw(form_password.encode(), user.password.encode()):
#                 # si obtenemos True después de validar la contraseña, podemos poner la identificación del usuario en la sesión
#                     messages.success(request, 'Bienvenido')
#                     request.session['usuario'] = { 'nombre' : user.nombre, 'username' : user.username, 'email' : user.email, 'id' : user.id}
#                     iduser = request.session['usuario'] 
#                     id2=iduser['id']
#                     return redirect(f"/acceso/added/{id2}")
#                 else:
#                     messages.error(request, 'Contraseña o username incorrecto')
#             else:
#                 messages.error(request, 'Contraseña o username incorrecto')
                
#             return redirect(reverse('acceso:acceso'))
#         else:
            
#             contexto = {
#                 'formRegister': UsuarioForm(),
#                 'formLogin': form,
#             }
#             return render(request, 'acceso/login.html', contexto) 

# def logout(request):
    
#     if 'usuario' in request.session:
#         messages.success(request, 'Vuelve pronto')
#         del request.session['usuario']
#     else:
#         messages.error(request, 'No estas logeado')
#     return redirect(reverse('acceso:acceso'))

            # if not request.user.email.endswith('@acme.com'):
            #     messages.error(request, f"No eres parte de nuestra compañia")
            #     return render(request, 'acceso/register.html', context={} )
            # else: