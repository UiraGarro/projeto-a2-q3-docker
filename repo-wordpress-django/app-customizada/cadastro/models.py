from django.db import models

from django.db import models

class Registro(models.Model):
    nome = models.CharField(max_length=100)
    mensagem = models.CharField(max_length=255)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome