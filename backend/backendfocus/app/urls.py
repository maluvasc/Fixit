from django.urls import path
from . import views
# Define as rotas específicas da aplicação.

urlpatterns = [
    path('', views.VideoListView.as_view(), name='video-list'),
    path('upload/', views.VideoUploadView.as_view(), name='video-upload'),
    path('repositorios/', views.RepositorioListCreate.as_view(), name='repositorio-list'),
    path('repositorios/delete/<int:pk>/', views.RepositorioDelete.as_view(), name='delete-repositorio'),
]