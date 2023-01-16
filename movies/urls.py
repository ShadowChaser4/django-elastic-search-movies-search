
from django.urls import path, include
from .views import MovieSearchView



urlpatterns = [
   path('movies/', MovieSearchView.as_view())
]


