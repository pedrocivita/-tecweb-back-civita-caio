from django.shortcuts import render
from .models import Movie
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .serializer import MovieSerializer

def index():
    return render("server")

@api_view(['GET', 'POST'])
def movies(request):
    if request.method == 'POST':
        newMovie = Movie(title = request.data['title'])
        newMovie.save()
    try:
        movies = Movie.objects.all()
        print(movies)
    except Movie.DoesNotExist:
        raise Http404()
    Serialized_movies = MovieSerializer(movies, many=True)
    return Response(Serialized_movies.data)

@api_view(['GET', 'POST'])
def movie(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        raise Http404()
    
    if request.method == 'POST':
        new_movie_data = request.data
        movie.title = new_movie_data['title']
        movie.fav = new_movie_data['fav']
        movie.save()

    serialized_movie = MovieSerializer(movie)
    return Response(serialized_movie.data)