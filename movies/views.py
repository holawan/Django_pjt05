from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views.decorators.http import require_safe
from .models import Movie
from django.core.paginator import Paginator

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.order_by('-pk')
    paginator = Paginator(movies, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'movies' : page_obj,
    }

    return render(request,'movies/index.html',context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genres = movie.genres.all()
    context = {
        'movie': movie,
        'genres': genres
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request,movie_pk):
    main_movie = get_object_or_404(Movie,pk=movie_pk)
    genres = main_movie.genres.all()
    recommend_movies = {}
    for genre in genres :
        recommend_movies[genre] = get_list_or_404(Movie,genres=genre.pk)[:10]
    context = {
        'movies':recommend_movies,
        'main_movie':main_movie
        }
    
    return render(request,'movies/recommended.html',context)
