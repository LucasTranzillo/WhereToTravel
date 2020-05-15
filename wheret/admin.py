from django.contrib import admin
from .models import User, Places, Stories

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'age')

class PlacesAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

class StoriesAdmin(admin.ModelAdmin):
    list_display = ('type', 'title')

admin.site.register(User, UserAdmin)
admin.site.register(Places, PlacesAdmin)
admin.site.register(Stories, StoriesAdmin)


