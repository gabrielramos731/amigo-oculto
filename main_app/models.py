from django.db import models

class Grupo(models.Model):
    nome = models.CharField(max_length=50)
    participante = models.CharField(max_length=50)
    