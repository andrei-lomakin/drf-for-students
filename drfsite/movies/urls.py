from django.urls import path
from .views import *

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movie/add/', MovieCreateView.as_view(), name='movie_add'),
    path('movie/edit/<int:pk>/', MovieUpdateView.as_view(), name='movie_edit'),
    path('movie/delete/<int:pk>/', MovieDeleteView.as_view(), name='movie_delete'),
    path('api/v1/movies/', MovieListCreateAPI.as_view(), name='movie_list_create_api'),
    path('api/v1/movies/<int:pk>/', MovieRetrieveUpdateDestroyAPI.as_view(), name='movie_detail_api'),
]