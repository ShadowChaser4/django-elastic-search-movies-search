from django.db import models 

from .actor import Artist


class Movie(models.Model): 
    name = models.CharField(max_length= 150)
    description = models.TextField( max_length=400 )
    release_date = models.DateField() 
    actors  = models.ManyToManyField(Artist)
    
    class Meta: 
        app_label = 'movies'
    