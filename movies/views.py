from django.shortcuts import render
# Create your views here.

from .documents import MovieDocument , ArtistDocument
from .seralizer import MovieSeralizer, ArtistSeralizer
from rest_framework.views import APIView
from rest_framework.response import Response
from elasticsearch_dsl import Q

class MovieSearchView(APIView): 
    seralizer_class = MovieSeralizer
    document_class = MovieDocument
    
    def generate_q_expression(self, query): 
        return Q(
            'bool', 
            should = [
                Q('match',  name={'query': query, 'fuzziness': 2}), 
                Q('nested', path = 'actors', 
                  query = Q('match', actors__first_name = {'query': query, 'fuzziness': 2})
                )
            ]
        )
    
    def get(self, request): 
        query = request.GET.get('query', '')
        q = self.generate_q_expression(query)
        search = self.document_class.search().query(q)
        
        res = search.execute()
        
        seralizer = self.seralizer_class(res, many = True)
        
        return Response(data= seralizer.data )
        
    
