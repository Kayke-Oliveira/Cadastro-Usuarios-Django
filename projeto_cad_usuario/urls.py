from django.urls import path
from app_cad_usuario import views

urlpatterns = [
    #rota

    #view responsável

    #nome referência
    path('', views.home,name='home'),
    path('usuarios/', views.usuarios,name='listagem_usuarios')
]
