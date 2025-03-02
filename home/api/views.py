from django.shortcuts import render
from  main import buscar_artigos
# Create your views here.

def exibir_artigos(request):
    palavra_chave = request.GET.get('q', 'tecnologia')
    artigos = buscar_artigos(palavra_chave)

    if artigos:
        return render(request, 'artigos.html', {'artigos': artigos, 'palavra_chave': 'palavra_chave'})
    else:
        return render(request, 'artigos.html', {'erro': 'Nenhum artigo encontrado.'})

def exibir_artigos_busca(request):
    palavra_chave = request.GET.get('q', '')  # Pega a palavra-chave da URL (ex: ?q=tecnologia)
    
    if palavra_chave:
        artigos_encontrados = buscar_artigos(palavra_chave)
        return render(request, 'index.html', {'artigos_encontrados': artigos_encontrados, 'palavra_chave': palavra_chave})
    else:
        return render(request, 'index.html', {'erro': 'Por favor, forneça uma palavra-chave para busca.'})