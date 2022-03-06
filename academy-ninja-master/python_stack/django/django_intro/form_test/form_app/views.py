from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    
    if request.method == "GET":}
        return render(request,"form_app/index.html")
    
    if request.method == "POST":
        print(request.POST)
        #PROCESAREMOS EN BASE DE DATOS
        email_from_form = request.POST.get('email', None) #primera forma de llamar los datos, me permite que si no trae valor, asignarle uno
        pwd_from_form = request.POST['pwd']  #segunda forma de llamar los datos del formulario
        
        print(f"A la base de datos {email_from_form} {pwd_from_form}")
        
        contexto = {
            'email': email_from_form,
            'pwd': pwd_from_form,
            'check': request.POST.get('check', False),  
        }
        
        print('*'*10,contexto)
        request.session['usuario'] = contexto
        
        
        # request.session['email'] = email_from_form
        # request.session['pwd'] = pwd_from_form
        # request.session['check'] = request.POST['check']
        
        return redirect("/success")
    
def resultados(request):
    return render(request,"form_app/resultados.html")
        

# def create_user(request):
#     print("Got Post Info....................")
#     print('*'*20,request.POST)
#     email_from_form = request.POST["email"]
#     pwd_from_form = request.POST["pwd"]
#     check_from_form = request.POST["check"]
#     print(email_from_form)
#     print(pwd_from_form)
#     print(check_from_form)
#     return redirect("/resultado")
    
    # return render(request,"form_app/success.html")
    

# def success(request):
#     return render(request,"form_app/success.html")

# def some_function(request):
#     request.session['email'] = request.POST['name']
#     request.session['counter'] = 100


