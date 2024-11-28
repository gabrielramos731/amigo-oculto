from django.urls import path
from .views import (CriarNovoGrupo,
                    # AddParticipantes
                    )

urlpatterns = [
    path('', CriarNovoGrupo.as_view(), name='novo_grupo'),
    # path('', AddParticipantes.as_view(), name='novo_participante'),
]
