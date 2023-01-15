from django.db import models


class Artist(models.Model): 
    first_name = models.CharField(max_length= 50)
    middle_name = models.CharField(max_length= 50, null= True, blank= True)
    last_name = models.CharField(max_length= 50)
    
    class Meta: 
        app_label = 'movies'
    
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name