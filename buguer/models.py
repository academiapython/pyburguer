from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.TextField(null=False, blank=False, default="")
    descricao = models.TextField(null=False, blank=False)
    preco = models.FloatField(null=False, blank=False)
    imagem = models.ImageField(upload_to='buguer/img', default='', null=False, blank=False)

    def __str__(self):
        return self.nome