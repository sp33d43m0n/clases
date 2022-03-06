from django.urls import path     
from . import views
from . import views_regalos
from .views import LoginView, login
# from . import views_forms

# http://127.0.0.1:8000/acceso/
app_name = 'acceso'

urlpatterns = [
    path('', LoginView.as_view(), name='acceso'),
    path('logout/', views.logout, name='logout'),
    path('login/', login, name='validar'),
    path('added/<int:id>', views_regalos.added , name='added'),
    path('added/editar/<int:id>', views_regalos.editar , name='edit'),
    path('added/borrar/<int:id>', views_regalos.borrar , name='borrar'),
    path('added/otorgar/<int:id>', views_regalos.otorgar , name='otorgar'),
    path('added/makeawish', views_regalos.makeawish , name='wish'),
    path('added/like/<int:id>', views_regalos.like , name='like'),

]

