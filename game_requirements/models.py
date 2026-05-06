from django.db import models
from games.models import Game


class Requirement(models.Model):
    game = models.OneToOneField(
        Game,
        on_delete=models.CASCADE,
        related_name='requirement',
        verbose_name='Jogo',
        db_index=True
    )
    system = models.CharField(
        max_length=255, 
        verbose_name='Sistema Operacional'
    )
    minimum_processor = models.CharField(
        max_length=255, 
        verbose_name='Processador Mínimo'
    )
    minimum_ram = models.IntegerField(
        default=0, 
        verbose_name='Memória RAM Mínima'
    )
    minimum_gpu = models.CharField(
        max_length=255, 
        verbose_name='GPU Mínima'
    )
    minimum_gpu_ram = models.IntegerField(
        default=0, 
        verbose_name='Memória GPU Mínima'
    )
    maximum_processor = models.CharField(
        max_length=255, 
        verbose_name='Processador Máximo'
    )
    maximum_ram = models.IntegerField(
        default=0, 
        verbose_name='Memória RAM Máxima'
    )
    maximum_gpu = models.CharField(
        max_length=255, 
        verbose_name='GPU Máxima'
    )
    maximum_gpu_ram = models.IntegerField(
        default=0, 
        verbose_name='Memória GPU Máxima'
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
        verbose_name = 'Requisito'
        verbose_name_plural = 'Requisitos'

    def __str__(self):
        return f"Requisito - {self.created_at.strftime('%Y/%m/%d %H:%M:%S')}"

