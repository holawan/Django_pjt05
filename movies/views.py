from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import *


# Create your views here.
@require_safe
def index(request):
    pass


@require_safe
def detail(request, movie_pk):

    return render(request, 'movies/detail.html')


@require_safe
def recommended(request):
    pass