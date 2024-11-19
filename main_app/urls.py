from django.urls import path
from .views import CriaNovoGrupo

urlpatterns = [
    path('', CriaNovoGrupo.as_view(), name='novo_grupo'),
]
