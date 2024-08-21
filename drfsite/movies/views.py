from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movie

from rest_framework import generics
from .serializers import MovieSerializer


class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'


class MovieCreateView(CreateView):
    model = Movie
    template_name = 'movies/movie_form.html'
    fields = ['title', 'description', 'year', 'director', 'genre', 'poster']
    success_url = reverse_lazy('movie_list')


class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'movies/movie_form.html'
    fields = ['title', 'description', 'year', 'director', 'genre', 'poster']
    success_url = reverse_lazy('movie_list')


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')


# ---------------- API ----------
class MovieListCreateAPI(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
