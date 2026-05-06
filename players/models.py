from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='player_profile',
        verbose_name='Usuário'
    )
    avatar_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='Avatar URL'
    )
    avatar_path = models.CharField(
        blank=True,
        null=True,
        verbose_name='Avatar caminho'
    )
    processor = models.CharField(
        max_length=255,
        verbose_name='Processador'
    )
    memory_ram = models.IntegerField(
        default=0,
        verbose_name='Memória RAM'
    )
    disk = models.CharField(
        max_length=50,
        verbose_name='SSD/HDD'
    )
    disk_space = models.IntegerField(
        default=0,
        verbose_name='Espaço em Disco'
    )
    unit = models.CharField(
        max_length=10,
        default='GB',
        verbose_name='Unidade de Medida'
    )
    gpu_name = models.CharField(
        max_length=255,
        verbose_name='Placa de Vídeo'
    )
    gpu_memory = models.IntegerField(
        default=0,
        verbose_name='Mémoria da Placa de Vídeo'
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
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        return f"{self.user.username}"