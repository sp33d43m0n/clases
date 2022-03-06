from django.urls import path     
from . import views

#http://127.0.0.1:8000/
urlpatterns =[
    path('', views.index),
    path('hello', views.hola),
    path('greet', views.saludar),
    path('saludar/<str:nombre>', views.saludar_nombre),
    #uan ruta apunta a una vista y le puede introducir parametros
    path('xavi/crea/ruta/funcion/<int:cantidad>/hecha/django', views.aumenta),
    path('editar/<int:id>',views.editar),
    # path('template', views.template),
]