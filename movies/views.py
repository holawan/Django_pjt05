from django.shortcuts import get_list_or_404, render
from django.views.decorators.http import require_safe
from .models import Movie


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.order_by('-pk')

    context = {
        'movies' : movies 
    }

    return render(request,'movies/index.html',context)


@require_safe
def detail(request, movie_pk):

    return render(request, 'movies/detail.html')


@require_safe
def recommended(request):
    pass