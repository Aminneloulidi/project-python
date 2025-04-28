from django.shortcuts import render
from .models import Photo   
def galerie(request):
    photos = Photo.objects.all()
    return render(request, 'photos/galerie.html', {'photos': photos})

# Create your views here.
