from django.views.generic import (FormView,
                                  ListView,
                                  CreateView,
                                  View,
                                  DetailView,
                                  UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy, reverse
from .models import Grupo, Participante
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

    def get_success_url(self):
        return reverse('detail_grupo', kwargs={'pk': self.object.pk})
    
class CriarNovoGrupoGet(ListView):
    model = Grupo
    template_name = 'novo_grupo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["grupo_form"] = NovoGrupoForm()
        return context

class GrupoUpdateView(UpdateView):
    model = Grupo
    template_name = 'update_grupo.html'
    fields = ['nome']
    
    def get_success_url(self):
        return reverse('detail_grupo', kwargs={'pk': self.object.pk})
    
class GrupoDeleteView(DeleteView):
    model = Grupo
    template_name = 'delete_grupo.html'

    def get_success_url(self):
        return reverse('novo_grupo')
    
class GrupoDetailView(DetailView):
    model = Grupo
    template_name = 'detail_grupo.html'