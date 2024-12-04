from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.


def index(req):
    movies = Movie.objects.all()

    return render(req, 'movies/index.html', {'movies': movies})
