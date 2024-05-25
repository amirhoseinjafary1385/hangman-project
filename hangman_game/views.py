from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'hangman_game/index.html')

def play(request):

    return render(request, 'hangman_game/play.html')

    
# Create your views here.
