from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ModelViewSet
from .models import (
    VideoGame, Platform,
    Publisher, Genre,
    Tag, Category,
    VideogameImage, Post,
)
from .permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly
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
    queryset = VideogameImage.objects.select_related('videogame').all()
    serializer_class = VideogameImageSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        game_id = self.request.query_params.get('game_id')
        if game_id:
            return VideogameImage.objects.filter(game_id=game_id)
        return super().get_queryset()



class PostViewSet(ModelViewSet):
    queryset = Post.objects.select_related('game', 'author').all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PlatformViewSet(ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    permission_classes = [IsAdminOrReadOnly]

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnly]

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminOrReadOnly]

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [IsAdminOrReadOnly]



