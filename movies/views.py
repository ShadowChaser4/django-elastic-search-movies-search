from django.shortcuts import render

# Create your views here.
from django_elasticsearch_dsl_drf.constants import *
from django_elasticsearch_dsl_drf.filter_backends import * 
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination

from .documents import MovieDocument , ArtistDocument
from .seralizer import MovieSeralizer, ArtistSeralizer

class MovieDocumentViewSet(BaseDocumentViewSet): 
    """ The base document viewset """
    
    document = MovieDocument
    serializer_class = MovieSeralizer
    pagination_class  = PageNumberPagination
    search_fields = {
        'name', 
        'release_date', 
        'actors'
    }    
    ordering = ('release_date' , 'name')