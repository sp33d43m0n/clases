from medico.models import *
from django.views import View
from django.shortcuts import render, HttpResponse, redirect
from medico.forms import MedicoForm
from django.contrib import messages
from django.urls import reverse
from medico.models import Medico



# Create your views here.
class MedicosView(View):
    def get(self, request):
        contexto = {
            'formModel': MedicoForm(),
            'medicos': Medico.objects.all(),
        }
        return render(request, 'medico/index.html', contexto )
        
    def post(self, request):
        form = MedicoForm(request.POST) #cargar los datos al formulario
        
        if form.is_valid():
            form.save()
            messages.success(request, 'usuario agregado correctamente')
            return redirect(reverse('medico:index'))
        else:
            messages.error(request, 'con errores, solucionar')
            return render(request, 'medico/index.html', { 'formModel': form })  #devolver el mismo form, para no cargar uno nuevo
        
class MedicosDetail(View):
    def get(self, request, id):
        medico = Medico.objects.get(id=id)
        form = MedicoForm(instance=medico)
        
        contexto = {
            'formModel': MedicoForm(),
            'medicos': Medico.objects.all(),
        }
        
        return render(request, 'medico/index.html', contexto)
        
    def post(self, request, id):
        medico = Medico.objects.get(id=id)
        form = MedicoForm(request.POST, instance=medico) #cargar los datos al formulario
        
        if form.is_valid():
            form.save()
            messages.success(request, 'usuario editado correctamente')
            return redirect(reverse('medico:index'))
        else:
            messages.error(request, 'con errores, solucionar')
            return render(request, 'medico/index.html', { 'formModel': form })  #devolver el mismo form, para no cargar uno nuevo        