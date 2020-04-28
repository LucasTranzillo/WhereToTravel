from django.urls import path
from .views import index, aboutus, contact, countriesB, countriesH, bplaces, hplaces, stories


urlpatterns = [
    path('', index),
    path('aboutus', aboutus),
    path('contact', contact),
    path('countriesB', countriesB),
    path('countriesH', countriesH),
    path('bplaces', bplaces),
    path('hplaces', hplaces),
    path('stories', stories),
]