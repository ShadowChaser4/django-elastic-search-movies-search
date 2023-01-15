
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieDocumentViewSet


router = DefaultRouter()
movies = router.register(r'movies', MovieDocumentViewSet, basename= 'moviedocument')

urlpatterns = [
     path(r'', include(router.urls)),
]


