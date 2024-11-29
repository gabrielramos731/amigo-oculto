from django.forms import ModelForm
from .models import Grupo, Participante

class NovoGrupoForm(ModelForm):
    class Meta:
        model = Grupo
        fields = ('nome',)
        
class AddParticipanteForm(ModelForm):
    class Meta:
        model = Participante
        fields = ('nome','telefone',)
        