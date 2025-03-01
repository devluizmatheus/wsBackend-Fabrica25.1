from django.db import models
from autenticacao.models import CustomUser
# Create your models here.

class Article(models.Model):
    title = models.CharField('Title', max_length=255)
    abstract = models.TextField('Resumo')
    content = models.TextField('Conteúdo Principal')
    pub_date = models.DateTimeField('Data de Publicação', auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    section = models.CharField('Seção', max_length=100)
    image_url = models.URLField(blank=True, null=True)
    image_root = models.TextField()

    def __str__(self):
        return self.title
