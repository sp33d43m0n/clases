from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('camion/<int:id>', views.camion, name='camion'),
    path('camiones/', views.camiones, name='camiones'),
    path('rutas/', views.rutas, name='rutas'),
    path('firstpage/', views.process1),
    path('secondpage/', views.process2),
    path('choferes/', views.choferes, name='choferes'),	
    path('chofer/<int:id>', views.chofer, name='chofer'),
    path('chofer/<int:id>/add/camion/', views.chofer_add_camion, name='chofer_add_camion'),
    path('chofer/remove/<int:id1>/<int:id2>/', views.chofer_remove_camion, name='chofer_remove'),   
]