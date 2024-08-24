from django import forms
from .models import Artista, Album
import requests

def pega_genero():
    response = requests.get('https://binaryjazz.us/wp-json/genrenator/v1/genre/')
    genero_aleatorio = response.content.decode('utf-8')[1:-1]
    return genero_aleatorio

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nome', 'endereco_pagina', 'qtd_integrantes', 'genero']

    def __init__(self, *args, **kwargs):
        super(ArtistaForm, self).__init__(*args, **kwargs)
        self.fields['genero'].initial = pega_genero()


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['nome_album', 'ano_lancamento', 'artista']
