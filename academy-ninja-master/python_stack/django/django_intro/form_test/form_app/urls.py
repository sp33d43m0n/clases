from django.urls import path     
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('success', views.resultados, name='success'),	
    # path('users', views.create_user),
    # path('resultado', views.success),  
]