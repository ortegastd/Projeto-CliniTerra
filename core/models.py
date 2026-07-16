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
    TIPO_CHOICES = [
        ('clinico_geral', 'Clínico Geral'),
        ('cardiologia', 'Cardiologia'),
        ('dermatologia', 'Dermatologia'),
        ('pediatria', 'Pediatria'),
        ('ortopedia', 'Ortopedia'),
        ('outro', 'Outro'),
    ]

    id_consulta = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='consultas')
    tipo = models.CharField(max_length=30, choices=TIPO_CHOICES, default='clinico_geral')
    data = models.DateField()
    hora = models.TimeField()
    observacoes = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ['data', 'hora']

    def __str__(self):
        return f"{self.usuario.nome} - {self.get_tipo_display()} ({self.data} {self.hora})"