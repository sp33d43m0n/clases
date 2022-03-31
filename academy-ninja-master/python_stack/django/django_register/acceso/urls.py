from django.urls import path
from . import views
from .views import LoginView 
from decorator_include import decorator_include    


# from . import views_forms

# http://127.0.0.1:8000/
app_name = 'acceso'

# urlpatterns = [
#     path('', views.indexcore, name='index'),	   
# ]

urlpatterns = [
    path('', LoginView.as_view(), name='acceso'),
    path('logedadmin/', views.logedadmin, name='logedadmin'),
    path('logeduser/', views.logeduser, name='logeduser'),
    path('logeduser/added/<int:idname>', views.logeduser, name='logeduser2'),
    #path('adminlog/', views.login_admin, name='loginadmin'),
    path('login_admin', views.login_admin, name='login_admin'),
    path('loginlocalbd/', views.loginbdlocal, name='loginlocalbd'),
    path("logout", views.logout_request, name="logout"),
    path('test1/', views.active, name='active'),
    path('test2/', views.link1, name='link1'),
    path('test3/', views.link2, name='link2'),
    

]



