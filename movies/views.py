from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Movie
from .forms import ReviewForm


class MoviesView(ListView):
    # spisok filmov

    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movies.html"


class MovieDetailView(DetailView):
    # polnoe opisanie film

    model = Movie
    slug_field = "url"
