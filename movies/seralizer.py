from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import MovieDocument, ArtistDocument


class MovieSeralizer(DocumentSerializer): 
    class Meta: 
        document = MovieDocument 
        fields = ("__all__")
        
        
class ArtistSeralizer(DocumentSerializer): 
    class Meta: 
        document = ArtistDocument
        fields = ("__all__")