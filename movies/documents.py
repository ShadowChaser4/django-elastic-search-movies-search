from django_elasticsearch_dsl import Document, fields 
from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl.registries import registry 
from .models import Movie, Artist

autocomplete_analyzer = analyzer(
    'autocomplete', 
    tokenizer = 'standard', 
    filter  = ['lowercase', 'edge_ngram'],
    type = 'custom', 
    filter_settings = {
        'edge_ngram': {
            'type': 'edgeNGram', 
            'min_gram': 1, 
            'max_gram': 10
        }
    }
)



@registry.register_document 
class ArtistDocument(Document): 
    first_name = fields.TextField(
        analyzer = autocomplete_analyzer
    )
    middle_name = fields.TextField(
        analyzer = autocomplete_analyzer
    )
    last_name = fields.TextField(
        analyzer = autocomplete_analyzer
    )
    class Index: 
        name = 'artist'
        settings = {
            'number_of_shards': 1, 
            'number_of_replicas': 0
        }
    class Django: 
        model = Artist

@registry.register_document 
class MovieDocument(Document): 
    actors = fields.NestedField(properties = {
             'id': fields.IntegerField(),
            'first_name': fields.TextField(), 
            'middle_name': fields.TextField(), 
            'last_name': fields.TextField(),
            }
    )
    
    name = fields.TextField(
        fields = {
            'raw': fields.TextField(analyzer = 'keyword')
        }
    )
    description = fields.TextField()
    class Index: 
        name = 'movies'
        settings = { 
                    'number_of_shards': 1, 
                    'number_of_replicas': 0
                    }
    class Django: 
        model = Movie
        related_models = [Artist, ]
        
    def get_instances_from_related(self, related_instance): 
        return related_instance.movie_set.all()