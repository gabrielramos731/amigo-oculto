from django.urls import path
from .views import (CriarNovoGrupo,
                    GrupoDetailView,
                    GrupoUpdateView,
                    GrupoDeleteView,
                    )

urlpatterns = [
    path('', CriarNovoGrupo.as_view(), name='novo_grupo'),
    path('<int:pk>/', GrupoDetailView.as_view(), name='detail_grupo'),
    path('<int:pk>/renomear', GrupoUpdateView.as_view(), name='update_grupo'),
    path('<int:pk>/deletar', GrupoDeleteView.as_view(), name='delete_grupo'),
]
