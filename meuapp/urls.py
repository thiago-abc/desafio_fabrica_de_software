from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('artistas/', views.artistas_view, name='artistas'),
    path('artistas/detalhes/<int:id>', views.detalhes, name='detalhes'),
    path('artistas/adiciona_artista/', views.adiciona_artista, name='adiciona_artista'),
    path('albuns/', views.albuns_view, name='albuns'),
    path('albuns/detalhes/<int:id>', views.detalhes_album, name='albuns'),
    path('albuns/adiciona_album/', views.adiciona_album, name='adiciona_album'),
]