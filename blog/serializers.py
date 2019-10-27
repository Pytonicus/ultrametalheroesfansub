from django.contrib.auth.models import User, Group
from .models import Entrada, Comentario, Serie
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = []


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class EntradaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entrada
        fields = ['autor','titulo', 'contenido','informacion','imagen','enlace','fecha']

class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comentario
        fields = ['entrada', 'autor', 'texto', 'fecha_publicacion', 'aprovado']

class SerieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Serie
        fields = ['titulo','poster','capturaUno','capturaDos','capturaTres','capturaCuatro','creador','franquicia','emision','episodios','sipnosis','enlace','activa']
