from django.db import models

class Grupo(models.Model):
    nome = models.CharField(max_length=50)
    codigo = models.CharField(max_length=6, null=True)
    participantes = models.ForeignKey("Participante",
                                             on_delete=models.CASCADE,
                                             null=True)

    def __str__(self):
        return self.nome
    
    
class Participante(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.nome
    