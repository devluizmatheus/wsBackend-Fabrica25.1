from django.db import models
from django.utils import timezone
from autenticacao.models import CustomUser
# Create your models here.

class Article(models.Model):
    titulo = models.CharField('Titulo', max_length=255)
    resumo = models.TextField('Resumo')
    conteudo_principal = models.TextField('Conteúdo Principal')
    data_publicacao = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    secao = models.CharField('Seção', max_length=100)
    image_url = models.URLField(blank=True, null=True)
    image_root = models.TextField()

    def __str__(self):
        return self.title
