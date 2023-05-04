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
    try:
        movies = Movie.objects.all()
    except Movie.DoesNotExist:
        raise Http404()
        
    if request.method == 'POST':
        if request.data['title'] in [movie.title for movie in movies]:
            return Response({'error': 'Movie already exists'})
        else:
            newMovie = Movie(title = request.data['title'])
            newMovie.save()
    Serialized_movies = MovieSerializer(movies, many=True)
    return Response(Serialized_movies.data)

@api_view(['GET', 'POST', 'DELETE'])
def movie(request, title):
    try:
        movie = Movie.objects.get(title=title)
    except Movie.DoesNotExist:
        raise Http404()
    if request.method == 'DELETE':
        movie.delete()

    serialized_movie = MovieSerializer(movie)
    return Response(serialized_movie.data)