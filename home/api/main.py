import requests
import random
from googletrans import Translator
from django.conf import settings

def gerador_artigos():
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    params = {
        "api-key": settings.NYT_API_KEY,
        "sort": "newest",  # Garantir que estamos pegando os artigos mais recentes
        "page": 1 
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        artigos = response.json()['response']['docs']
        artigos = random.sample(artigos, min(5, len(artigos)))  # Seleciona aleatoriamente 5 artigos
        
        artigos_traduzidos = traduzir_artigos(artigos)
        return artigos_traduzidos
    else:
        return None

# Função para buscar artigos com palavra-chave
def buscar_artigos(palavra_chave):
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    params = {
        "q": palavra_chave,
        "api-key": settings.NYT_API_KEY
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()['response']['docs']
    else:
        return None

# Função para traduzir os artigos
def traduzir_artigos(artigos):
    translator = Translator()
    artigos_traduzidos = []
    
    for artigo in artigos:
        
        titulo_traduzido = translator.translate(artigo['headline']['main'], src='en', dest='pt').text
        resumo_traduzido = translator.translate(artigo['abstract'], src='en', dest='pt').text if artigo.get('abstract') else ''
    
        artigo_traduzido = {
            'titulo': titulo_traduzido,
            'resumo': resumo_traduzido,
            'url': artigo['web_url']
        }
        
        artigos_traduzidos.append(artigo_traduzido)

    return artigos_traduzidos
