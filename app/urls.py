from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('remover/<int:id>/', views.remover, name='remover'),
    path('editar/<int:id>/', views.editar, name='editar'),
]
