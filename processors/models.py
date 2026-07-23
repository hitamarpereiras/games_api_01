from django.db import models


class Processor(models.Model):
    manufacturer= models.CharField(
        max_length=50,
        verbose_name="Fabricante"
    )
    modelo= models.CharField(
        max_length=50,
        verbose_name="Modelo"
    )
    generation= models.CharField(
        max_length=16,
        verbose_name="Geração"
    )
    year= models.IntegerField(
        default="2026",
        verbose_name="Ano"
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
        verbose_name = 'Pocessador'
        verbose_name_plural = 'Pocessadores'

    def __str__(self):
        return self.modelo
