from django import forms
from .models import Grupo, Participante

class NovoGrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nome']
        
class AddParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = ['nome','telefone']