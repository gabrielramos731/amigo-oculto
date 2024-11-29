from django.views.generic import (ListView,
                                  CreateView,
                                  View,
                                  DetailView,
                                  UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy, reverse
from .models import Grupo, Participante
from .forms import NovoGrupoForm, AddParticipanteForm

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

class GrupoDetailView(View):
    def get(self, request, *args, **kwargs):
        view = GrupoDetailGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = GrupoDetailPost.as_view()
        return view(request, *args, **kwargs)
    
class GrupoDetailGet(DetailView):
    model = Grupo
    template_name = 'detail_grupo.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_participante_form"] = AddParticipanteForm()
        context["participantes_list"] = Participante.objects.filter(grupo=self.kwargs['pk'])
        return context
    
    def get_queryset(self):
        return super().get_queryset()
    
class GrupoDetailPost(CreateView):
    model = Participante
    template_name = 'detail_grupo.html'
    fields = ['nome','telefone']
    
    def get_success_url(self):
        return reverse('detail_grupo', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        participante = form.save(commit=False)
        participante.grupo = Grupo.objects.get(pk=self.kwargs['pk'])
        form.save()
        return super().form_valid(form)
