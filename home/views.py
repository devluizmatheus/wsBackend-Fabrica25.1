from django.shortcuts import render, redirect,  get_object_or_404

from .forms import ArticleForm
from .models import Article
# Create your views here.

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

def list_article(request):
    article = Article.objects.filter(author=request.user)
    return render(request, 'listar_artigos', {'article': article})

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

def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk, author=request.user)
    article.delete()
    return redirect('deletar_artigos')
