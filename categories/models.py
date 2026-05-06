from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name='Nome da Categoria'
    )
    description = models.TextField(
        max_length=1000,
        default='Sem descrição',
        verbose_name='Descrição da categoria'
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
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name