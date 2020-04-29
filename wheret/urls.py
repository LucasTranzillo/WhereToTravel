from django.urls import path
from .views import index, aboutus, contact, bplaces, hplaces, stories


urlpatterns = [
    path('', index),
    path('index', index),
    path('aboutus', aboutus),
    path('contact', contact),
    path('bplaces', bplaces),
    path('hplaces', hplaces),
    path('stories', stories),
]