from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

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

