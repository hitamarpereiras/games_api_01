from django.db import models


class Gpu(models.Model):
    manufacturer= models.CharField(
        max_length=50,
        verbose_name="Fabricante"
    )
    modelo= models.CharField(
        max_length=100,
        verbose_name="Modelo"
    )
    year= models.IntegerField(
        default="2026",
        verbose_name="Ano"
    )
    vram= models.CharField(
        max_length=100,
        verbose_name="VRAM"
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
        verbose_name = 'GPU'
        verbose_name_plural = 'GPUs'

    def __str__(self):
        return self.modelo