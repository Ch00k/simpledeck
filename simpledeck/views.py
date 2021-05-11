from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from deck.models import Deck


def handler404(request: HttpRequest, exception: Exception = None) -> HttpResponse:
    return render(request, "404.html")


def demo(request: HttpRequest) -> HttpResponse:
    return render(request, "demo.html", {"themes": Deck.THEMES})
