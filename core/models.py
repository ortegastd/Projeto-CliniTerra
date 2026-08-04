from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    # ADICIONE ESTA LINHA ABAIXO:
    telefone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nome