
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse



def login_check(function):
    def wrap(request, *args, **kwargs):
        
        if 'usuario' not in request.session:
            messages.error(request, 'No estas logeado')
            return redirect(reverse('acceso:acceso'))
        
        return function(request, *args, **kwargs)
    return wrap