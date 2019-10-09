from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_entradas, name='lista_entradas'),
    path('entrada/<int:pk>/', views.entrada, name='entrada'),
    path('entrada/<int:pk>/comentario/', views.nuevo_comentario, name="nuevo_comentario"),
    path('series/activas/', views.series_activas, name="series_activas"),
    path('series/terminadas/', views.series_terminadas, name="series_terminadas")
]