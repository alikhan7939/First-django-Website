from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def home_view(request):
    return HttpResponse("<h1>Home</h1>")

def about_view(request):
    return HttpResponse("<h1>About</h1>")

def contacet_view(request):
    return HttpResponse("<h1>contacet</h1>")