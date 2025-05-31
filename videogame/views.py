from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ModelViewSet
from .models import (
    VideoGame, Platform,
    Publisher, Genre,
    Tag, Category,
    VideogameImage, Post,
)
from .permissions import IsAdminOrReadOnly
from .serializers import (
    VideogameImageSerializer,PlatformSerializer,
    GenreSerializer,TagSerializer,
    VideoGameSerializer,PublisherSerializer,
    CategorySerializer,PostSerializer,
)
# Create your views here.

class VideogameViewSet(ModelViewSet):
    queryset = VideoGame.objects.select_related( 'category', 'publisher').prefetch_related('tags', 'genre', 'platform', 'images').all()
    serializer_class = VideoGameSerializer
    permission_classes = [IsAdminOrReadOnly]


class VideogameImageViewSet(ModelViewSet):
    queryset = VideogameImage.objects.all()
    serializer_class = VideogameImageSerializer

    def get_queryset(self):
        game_id = self.request.query_params.get('game_id')
        if game_id:
            return VideogameImage.objects.filter(game_id=game_id)
        return super().get_queryset()


