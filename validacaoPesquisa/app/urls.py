from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_carro/', views.cadastrar_carro, name='cadastrar_carro'),
    path('listar_carro/', views.listar_carro, name='listar_carro'),
    path('editar_carro/<int:pk>', views.editar_carro, name='editar_carro'),
    path('remover_carro/<int:pk>', views.remover_carro, name='remover_carro'),
]