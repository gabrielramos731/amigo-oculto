from django.views.generic import (FormView,
                                  ListView,
                                  CreateView)
from django.urls import reverse_lazy
from .forms import NovoGrupoForm
from .models import Grupo

class CriaNovoGrupo(CreateView):
    model = Grupo
    template_name = 'novo_grupo.html'
    fields = ['nome',]
    success_url = reverse_lazy('novo_grupo')
