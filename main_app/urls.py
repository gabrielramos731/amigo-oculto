from django.urls import path, include
from .views import (HomeView,
                    CriarNovoGrupo,
                    GrupoDetailView,
                    GrupoUpdateView,
                    GrupoDeleteView,
                    UpdateParticipanteView,
                    DeleteParticipanteView,
                    SignUpView,
                    geraSorteio,
                    )

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('grupo/', CriarNovoGrupo.as_view(), name='novo_grupo'),
    path('grupo/<str:encoded_pk>/', GrupoDetailView.as_view(), name='detail_grupo'),
    path('<str:encoded_pk>/renomear', GrupoUpdateView.as_view(), name='update_grupo'),
    path('<str:encoded_pk>/deletar', GrupoDeleteView.as_view(), name='delete_grupo'),
    path('<str:encoded_pk_grupo>/atualizar_participante/<str:encoded_pk_part>', UpdateParticipanteView.as_view(), name='update_participante'),
    path('<str:encoded_pk_grupo>/deletar_participante/<str:encoded_pk_part>', DeleteParticipanteView.as_view(), name='delete_participante'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('sorteio/<str:encoded_pk>', geraSorteio, name='sorteio'),
]
