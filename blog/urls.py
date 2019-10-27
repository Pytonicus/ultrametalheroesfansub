from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'entradas', views.EntradaViewSet)
router.register(r'comentarios', views.ComentarioViewSet)
router.register(r'series', views.SerieViewSet)

urlpatterns = [
    path('', views.lista_entradas, name='lista_entradas'),
    path('entrada/<int:pk>/', views.entrada, name='entrada'),
    path('entrada/<int:pk>/comentario/', views.nuevo_comentario, name="nuevo_comentario"),
    path('series/activas/', views.series_activas, name="series_activas"),
    path('series/terminadas/', views.series_terminadas, name="series_terminadas"),
    path('series/serie/<int:pk>/', views.serie, name="serie"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]