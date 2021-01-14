from django.shortcuts import render

from django.http import HttpResponse

from .models import City

# Create your views here.

def home(request):
  return render(request, 'home.html')


def about(request):
  return HttpResponse('<h1>About</h1>')