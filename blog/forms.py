from django import forms
from .models import Entrada, Comentario

class FormComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('autor', 'texto')