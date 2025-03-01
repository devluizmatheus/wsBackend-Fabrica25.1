from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    data_nascimento = models.DateField('Data Nascimento', blank=True, null=True)
    numero_telefone = models.CharField('Número de Telefone', max_length=50, blank=True)
    foto = models.TextField('Foto', blank=True, null=True)
    bio = models.TextField('Bio', blank=True, null=True)

     # Adicionando `related_name` para evitar conflitos nas relações reversas
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='customuser_set',  # Evita o conflito com a relação reversa
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='customuser_permissions_set',  # Evita o conflito com a relação reversa
        blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Create your models here.
