from django.urls import path     
from . import views
# from . import views_forms

# http://127.0.0.1:8000/app/
app_name = 'app'

urlpatterns = [
    path('', views.indexapp, name='root'),	   
]