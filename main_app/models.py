from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model

class Grupo(models.Model):
    nome = models.CharField(max_length=50)
    codigo = models.CharField(max_length=6, null=True)
    admin = models.ForeignKey(get_user_model(), 
                              on_delete=models.CASCADE,
                              null=True)

    def __str__(self):
        return self.nome
    
class Participante(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11,
                                validators=[MinLengthValidator(11)])
    grupo = models.ForeignKey(Grupo,
                              on_delete=models.CASCADE,
                              null=True,
                              related_name='participante')
    codigo_match = models.IntegerField(null=True)
    
    def __str__(self):
        return self.nome