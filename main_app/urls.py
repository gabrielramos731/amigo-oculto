from django.urls import path, include
from .views import (HomeView,
                    CriarNovoGrupo,
                    GrupoDetailView,
                    GrupoUpdateView,
                    GrupoDeleteView,
                    UpdateParticipanteView,
                    DeleteParticipanteView,
                    )

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('grupo/', CriarNovoGrupo.as_view(), name='novo_grupo'),
    path('grupo/<int:pk>/', GrupoDetailView.as_view(), name='detail_grupo'),
    path('<int:pk>/renomear', GrupoUpdateView.as_view(), name='update_grupo'),
    path('<int:pk>/deletar', GrupoDeleteView.as_view(), name='delete_grupo'),
    path('<int:pk_grupo>/atualizar_participante/<int:pk_part>', UpdateParticipanteView.as_view(), name='update_participante'),
    path('<int:pk_grupo>/deletar_participante/<int:pk_part>', DeleteParticipanteView.as_view(), name='delete_participante'),
]
