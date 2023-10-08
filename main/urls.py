from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
	path('', views.index, name='home'),
	path('Review/', views.review, name='review'),
    path('Categoria/', views.categorias, name= 'Categoria'),
    path('Gestion/', views.Gestion, name= 'Gestion'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
	]

    