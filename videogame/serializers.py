from rest_framework.serializers import ModelSerializer
from .models import (
VideoGame,Platform,
Publisher,Genre,
Tag,Category,
VideogameImage,Post,
)

class VideogameImageSerializer(ModelSerializer):
    class Meta:
        model = VideogameImage
        fields = ['id', 'videogame', 'image']

class PlatformSerializer(ModelSerializer):
    class Meta:
        model = Platform
        fields = ['id', 'name']

class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class VideoGameSerializer(ModelSerializer):
    images = VideogameImageSerializer(many=True, read_only=True)
    platform = PlatformSerializer(many=True)
    genre = GenreSerializer(many=True)
    tags = TagSerializer(many=True)
    class Meta:
        model = VideoGame
        fields = [
            'id', 'title','description',
            'platform','release_date','genre','images',
            'publisher','category','age_rating','tags',
            'created_at', 'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']



class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 'game','body', 'author',
            'created_at', 'updated_at'

        ]
        read_only_fields = ['created_at', 'updated_at', 'author']