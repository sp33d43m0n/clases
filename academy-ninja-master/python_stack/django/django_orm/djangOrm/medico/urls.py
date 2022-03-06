from django.urls import path     
from .views import MedicosView, MedicosDetail

# http://127.0.0.1:8000/medico/

app_name = 'medico'

urlpatterns = [
    path('', MedicosView.as_view(), name='index' ),
    path('<int:id>/', MedicosDetail.as_view(), name='editar' ),
]

