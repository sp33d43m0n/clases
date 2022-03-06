from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.
def root(request):
    print('*'*10,request)
    return redirect('/blogs')

def blogs(request):
    print('*'*10,request)
    return HttpResponse("Placeholder")
# preguntar que hace referencia...mostrar una lista de todos los blogs

def new(request):
    print('*'*10,request)
    return HttpResponse("Placeholder_New")

def create(request):
    print('*'*10,request)
    return redirect('/')

def show(request, number):
    print('*'*10,request, number)
    return HttpResponse(f'placeholder para mostrar el blog numero {number}')

def edit(request, number):
    print('*'*10,request, number)
    return HttpResponse(f'placeholder para editar el blog {number}')

def destroy(request, number):
    print('*'*10,request, number)
    return redirect('/')

def answertext(request):
    print('*'*10,request)
    responsedata = {'text': 'prueba de texto'}
    return JsonResponse(responsedata)