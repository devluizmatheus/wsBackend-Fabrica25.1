from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ArticleForm
from .models import Article
from api.views import exibir_artigos, exibir_artigos_busca
# Create your views here.


def home(request):
    
    noticiais_usuarios = Article.objects.all().order_by('-data_publicacao')[:5]

    noticiais_api = exibir_artigos

    buscar_noticiais_api = exibir_artigos_busca

    return render(request, 'home.html', {
        'noticia_usuarios': noticiais_usuarios,
        'noticiais_api': noticiais_api,
        'buscador_noticiais_api': buscar_noticiais_api
    }
        )

# CRUD
@login_required
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('listar_artigos')
    else:
        form = ArticleForm()
    return render(request, 'criar_artigos', {'form': form})

@login_required
def list_article(request):
    article = Article.objects.filter(author=request.user)
    return render(request, 'listar_artigos', {'article': article})

@login_required
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk, author=request.user)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('listar_artigos')
        
    else: 
        form = ArticleForm(instance=article)
    
    return render(request, 'editar_artigos', {'form': form, 'article': article})

@login_required
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk, author=request.user)
    article.delete()
    return redirect('deletar_artigos')
