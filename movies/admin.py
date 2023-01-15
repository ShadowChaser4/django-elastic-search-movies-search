from django.contrib import admin

# Register your models here.
from .models import Artist, Movie


admin.site.register(Artist)
admin.site.register(Movie)
