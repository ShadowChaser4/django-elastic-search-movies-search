
from django.urls import path
from .views import MovieSearchView, ActorsAutoCompleteSerach



urlpatterns = [
   path('movies/', MovieSearchView.as_view()), 
   path('actors/', ActorsAutoCompleteSerach.as_view())
]


