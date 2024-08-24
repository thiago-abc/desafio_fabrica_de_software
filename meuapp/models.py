from django.db import models
import requests

# def pega_genero():
#     response = requests.get('https://binaryjazz.us/wp-json/genrenator/v1/genre/')
#     genero_aleatorio = response.content.decode('utf-8')[1:-1]
#     return genero_aleatorio
#default=pega_genero()

class Artista(models.Model):
    nome = models.CharField(max_length=150)
    endereco_pagina = models.CharField(max_length=150)
    qtd_integrantes = models.IntegerField()
    genero = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return f"{self.nome} {self.endereco_pagina} {self.qtd_integrantes} {self.genero}"

class Album(models.Model):
    nome_album = models.CharField(max_length=150)
    ano_lancamento = models.DateField()
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome_album} {self.ano_lancamento} {self.artista}"