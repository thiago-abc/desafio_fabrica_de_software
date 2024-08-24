from django.contrib import admin

from meuapp.models import Artista, Album


# Register your models here.
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco_pagina', 'qtd_integrantes')

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('nome_album', 'ano_lancamento', 'artista_nome')

    def artista_nome(self, obj):
        return obj.artista.nome


admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Album, AlbumAdmin)
