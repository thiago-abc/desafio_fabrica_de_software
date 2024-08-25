from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Artista, Album
from .forms import ArtistaForm, AlbumForm
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view


def artistas_view(request):
    meusartistas = Artista.objects.values()
    template = loader.get_template('meusartistas.html')
    context = {'meusartistas': meusartistas}
    return HttpResponse(template.render(context, request))

def excluir_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        artista.delete()
        return redirect('lista_artistas')
    return render(request, 'confirmar_exclusao.html', {'artista': artista})

def editar_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('lista_artistas')
    else:
        form = ArtistaForm(instance=artista)

    return render(request, 'editar_artista.html', {'form': form, 'artista': artista})


def detalhes(request, id):
    meuartista = get_object_or_404(Artista, id=id)
    albuns = Album.objects.filter(artista=meuartista)
    #template = loader.get_template('detalhes.html')

    return render(request, 'detalhes.html', {
        'meuartista': meuartista,
        'albuns': albuns,
    })

def albuns_view(request):
    meusalbuns = Album.objects.values()
    template = loader.get_template('albuns.html')
    context = {'meusalbuns': meusalbuns}
    return HttpResponse(template.render(context, request))

def detalhes_album(request, id):
    meualbum = Album.objects.get(id=id)
    template = loader.get_template('detalhes_albuns.html')
    context = {'meualbum': meualbum}
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def adiciona_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meusartistas')
    else:
        form = ArtistaForm()
    return render(request, 'artista_form.html', {'form': form})

def adiciona_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('albuns')
    else:
        form = AlbumForm()

    return render(request, 'adicionar_album.html', {'form': form})


