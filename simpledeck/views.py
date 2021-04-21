from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def handler404(request: HttpRequest, exception: Exception = None) -> HttpResponse:
    return render(request, "404.html")
