from django.urls import path
from deseos2 import views

urlpatterns = [
		path('', views.index),
        path('reg_validate', views.reg_validate),
		path('login_validate', views.login_validate),
		path('home', views.home),
		path('logout', views.logout),
		path('bookss', views.AllBook),
		path('bookss/new', views.AddNewBook),
		path('bookss/create', views.CreateNewBook),
		path('bookss/<int:id>/', views.TvBook),
		path('bookss/<int:id>/edit', views.EditBook),
		path('bookss/<int:id>/update', views.UpdateBook),
		path('bookss/<int:id>/destroy', views.DeleteBook)
	]