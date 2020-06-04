from django.shortcuts import render
from wheret.models import Places, User, Stories
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

def index(request):
    placeList = Places.objects.all()
    context = {
        'places': placeList
    }
    return render(request, 'index.html', context)

def contact(request):
    form = ContactForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(request, "E-mail sent!")
            form = ContactForm
        else:
            messages.error(request, "Error!")
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

def bplaces(request):
    return render(request, 'bplaces.html')

def hplaces(request):
    return render(request, 'hplaces.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def stories(request):
    return render(request, 'stories.html')

