from django.db import models
from django.contrib.auth.models import User
from games.models import Game


class Review(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Usuário'
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='games',
        verbose_name='Jogo'
    )
    username = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        verbose_name='Username',
    )
    fps = models.IntegerField(
        default=60,
        verbose_name='FPS',
    )
    quality = models.CharField(
        max_length=50,
        verbose_name='Qualidade'
    )
    observation = models.TextField(
        blank=True,
        null=True,
        verbose_name='Observação'
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
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

    def __str__(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')
