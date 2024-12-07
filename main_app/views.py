import base64
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import (ListView,
                                  CreateView,
                                  View,
                                  DetailView,
                                  UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import forms
from django.contrib.auth.mixins import UserPassesTestMixin
from .utils import encode_pk, decode_pk
from .models import Grupo, Participante
from .forms import NovoGrupoForm, AddParticipanteForm

class HomeView(ListView):
    template_name = 'home.html'
    model = Grupo
    
class CriarNovoGrupo(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CriarNovoGrupoGet.as_view()
        return view(request, *args, **kwargs)
    
    def get_login_url(self) -> str:
        return reverse('login')
    
    def post(self, request, *args, **kwargs):
        view = CriarNovoGrupoPost.as_view()
        return view(request, *args, **kwargs)

class CriarNovoGrupoGet(ListView):
    model = Grupo
    template_name = 'novo_grupo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["grupo_form"] = NovoGrupoForm()
        return context
    
    def get_queryset(self) -> QuerySet[Grupo]:
        return Grupo.objects.filter(admin=self.request.user).only('nome')

class CriarNovoGrupoPost(CreateView):
    model = Grupo
    template_name = 'novo_grupo.html'
    fields = ['nome',]

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        obj = form.save(commit=False)
        obj.admin = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail_grupo', kwargs={'encoded_pk': encode_pk(self.object.pk)})

class GrupoUpdateView(LoginRequiredMixin, UpdateView):
    model = Grupo
    template_name = 'update_grupo.html'
    fields = ['nome']
    
    def get_object(self, queryset = None):
        encoded_pk = self.kwargs['encoded_pk']
        decoded_pk = decode_pk(encoded_pk)
        return get_object_or_404(Grupo, pk=decoded_pk)
        
    def get_success_url(self):
        return reverse('detail_grupo', kwargs={'encoded_pk': encode_pk(self.object.pk)})
    
    def get_login_url(self) -> str:
        return reverse('login')
    
class GrupoDeleteView(LoginRequiredMixin, DeleteView):
    model = Grupo
    template_name = 'delete_grupo.html'
    
    def get_object(self, queryset = None):
        encoded_pk = self.kwargs['encoded_pk']
        decoded_pk = decode_pk(encoded_pk)
        return get_object_or_404(Grupo, pk=decoded_pk)

    def get_success_url(self):
        return reverse('novo_grupo')
    
    def get_login_url(self) -> str:
        return reverse('login')

class GrupoDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = GrupoDetailGet.as_view()
        return view(request, *args, **kwargs)

    def get_login_url(self) -> str:
        return reverse('login')
    
    def post(self, request, *args, **kwargs):
        view = GrupoDetailPost.as_view()
        return view(request, *args, **kwargs)
    
class GrupoDetailGet(UserPassesTestMixin, DetailView):
    model = Grupo
    template_name = 'detail_grupo.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_participante_form"] = AddParticipanteForm
        context["participantes_list"] = Participante.objects.filter(grupo=decode_pk(self.kwargs['encoded_pk']))
        return context

    def get_object(self, queryset = None):
        encoded_pk = self.kwargs.get('encoded_pk')
        decoded_pk = decode_pk(encoded_pk)
        return get_object_or_404(Grupo, pk=decoded_pk)
    
    def test_func(self):
        grupo = self.get_object()
        return grupo.admin == self.request.user
                
class GrupoDetailPost(CreateView):
    model = Participante
    template_name = 'detail_grupo.html'
    form_class = AddParticipanteForm
    
    def get_success_url(self):
        return reverse('detail_grupo', kwargs={'encoded_pk': self.kwargs['encoded_pk']})

    def form_valid(self, form):
        participante = form.save(commit=False)
        participante.grupo = Grupo.objects.get(pk=decode_pk(self.kwargs['encoded_pk']))
        form.save()
        return super().form_valid(form)

class UpdateParticipanteView(LoginRequiredMixin, UpdateView):
    model = Participante
    template_name = 'update_participante.html'
    form_class = AddParticipanteForm
    
    def get_object(self, queryset=None):
        encoded_pk = self.kwargs['encoded_pk_part']
        decoded_pk = decode_pk(encoded_pk)
        return get_object_or_404(Participante, pk=decoded_pk)
    
    def get_success_url(self):
        return reverse_lazy('detail_grupo', kwargs={'encoded_pk': self.kwargs['encoded_pk_grupo']})
    
    def get_login_url(self) -> str:
        return reverse('login')

class DeleteParticipanteView(LoginRequiredMixin, DeleteView):
    model = Participante
    template_name = 'delete_participante.html'
    
    def get_object(self, queryset = None):
        encoded_pk = self.kwargs['encoded_pk_part']
        decoded_pk = decode_pk(encoded_pk)
        return get_object_or_404(Participante, pk=decoded_pk)
    
    def get_success_url(self):
        return reverse_lazy('detail_grupo', kwargs={'encoded_pk': self.kwargs['encoded_pk_grupo']})
    
    def get_login_url(self) -> str:
        return reverse('login')
    
class SignUpView(CreateView):
    model = forms.UserModel
    template_name = 'registration/signup.html'
    form_class = forms.UserCreationForm
    success_url = reverse_lazy("login")
