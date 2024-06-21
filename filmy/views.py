from django.shortcuts import render
#dotazovani DB
from filmy.models import Movie
# Create your views here.
def movies(request):
    context = {
        'movies': Movie.objects.all().order_by('name')
    }
    return render(request, 'filmy/movies.html', context)

def movie(request,id):
    context = {
        'movie': Movie.objects.get(id=id)
    }
    return render(request, 'filmy/movie.html', context)
def actors(request,id):
    context = {
        'actors': Actor.objects.all().order_by('name')
    }
    return render(request, 'filmy/actors.html', context)
def actor(request,id):
    context = {
        'actor': Actor.objects.get(id=id)
    }
    return render(request, 'filmy/actor.html', context)
