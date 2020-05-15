from django.shortcuts import render
from wheret.models import Places, User, Stories

# Create your views here.

def index(request):
    placeList = Places.objects.all()
    context = {
        'places': placeList
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def bplaces(request):
    return render(request, 'bplaces.html')

def hplaces(request):
    return render(request, 'hplaces.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def stories(request):
    return render(request, 'stories.html')

