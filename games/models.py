from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

class Game(models.Model):
    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='games',
        verbose_name='Usuário',
        db_index=True
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Nome de Jogo',
        unique=True,
        db_index=True
    )
    description = models.TextField(
        max_length=1000,
        default='Sem descrição',
        verbose_name='Descrição do jogo'
    )
    category = models.ManyToManyField(
        Category,
        related_name='games',
        verbose_name='Categoria',
        db_index=True
    )
    release_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de lançamento"
    )
    cover_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='Capa do jogo'
    )
    cover_path = models.CharField(
        blank=True,
        null=True,
        verbose_name='Caminho da imagem'
    )
    score = models.FloatField(
        default=0.0,
        verbose_name='Pontuação'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em',
    )

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'

    def __str__(self):
        return self.name
