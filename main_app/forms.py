from django.forms import ModelForm
from .models import Grupo

class NovoGrupoForm(ModelForm):
    class Meta:
        model = Grupo
        fields = ('nome',)
        