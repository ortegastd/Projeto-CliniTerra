from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    # ADICIONE ESTA LINHA ABAIXO:
    telefone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    data = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.tipo} - {self.paciente.nome}"