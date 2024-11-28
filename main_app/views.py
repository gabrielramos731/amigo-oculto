from django.views.generic import (FormView,
                                  ListView,
                                  CreateView,
                                  View)
from django.urls import reverse_lazy
from .models import Grupo
from .forms import NovoGrupoForm

class CriarNovoGrupo(View):
    def get(self, request, *args, **kwargs):
        view = CriarNovoGrupoGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CriarNovoGrupoPost.as_view()
        return view(request, *args, **kwargs)

class CriarNovoGrupoPost(CreateView):
    model = Grupo
    template_name = 'novo_grupo.html'
    fields = ['nome',]
    success_url = reverse_lazy('novo_grupo')
    
class CriarNovoGrupoGet(ListView):
    model = Grupo
    template_name = 'novo_grupo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["grupo_form"] = NovoGrupoForm()
        return context
