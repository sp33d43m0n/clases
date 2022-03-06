from django.shortcuts import render, HttpResponse

# Create your views here.

def indexapp(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")