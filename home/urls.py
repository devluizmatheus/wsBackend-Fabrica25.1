from django.urls import path

from .views import home

#CRUD 
from .views import create_article, list_article, edit_article, delete_article

urlpatterns = [
    path('', home, name="home"),
    path('criar/', create_article, name='criar_artigos'),
    path('list/', list_article, name='listar_artigos'),
    path('edit/<int:pk>', edit_article, name='editar_artigos'),
    path('excluir/<int:pk>', delete_article, name='excluir_artigos'),
]
