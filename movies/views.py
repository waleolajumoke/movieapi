from django.shortcuts import render
from .models import Movie 
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
def create_movie(request):
    movie = MovieSerializer(data=request.data)
    if movie.is_valid():
        movie.save()
        return Response(movie.data)

@api_view(['GET'])
def allmovies(request):
    movies = Movie.objects.all()
    record =  MovieSerializer(movies, many=True)
    return Response(record.data)

@api_view(['DELETE'])
def remove_movie(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return Response(' Movie deleted')

@api_view(['PUT'])
def edit_movie(request, id):
    movie = Movie.objects.get(id=id)
    info = MovieSerializer(data=request.data, instance=movie)
    if info.is_valid():
        info.save()
        return Response(info.data)


