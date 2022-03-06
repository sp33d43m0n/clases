from django.urls import path     
from . import views
from . import views_forms

# http://127.0.0.1:8000/core/

app_name = 'core'

urlpatterns = [
    path('', views.list_users, name='users'),
    path('add/', views.add_users, name='add_users'),
    path('edit/<int:id>', views.edit_users, name='edit_users'),
    path('delete/<int:id>', views.delete_users, name='delete_users'),
    path('add/forms/', views_forms.add_form, name='add_form'),
    path('edit/forms/<int:id>', views_forms.edit_form, name='edit_form'),
]


