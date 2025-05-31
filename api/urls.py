from django.urls import path
from rest_framework.routers import DefaultRouter
from videogame.views import (
    VideogameViewSet, VideogameImageViewSet, PostViewSet,PlatformViewSet,
    GenreViewSet,TagViewSet,CategoryViewSet,PublisherViewSet,
)




router = DefaultRouter()
router.register('videogames', VideogameViewSet)
router.register('images', VideogameImageViewSet)
router.register('posts', PostViewSet)
router.register('platforms', PlatformViewSet)
router.register('genres', GenreViewSet)
router.register('tags', TagViewSet)
router.register('categories', CategoryViewSet)
router.register('publishers', PublisherViewSet)
urlpatterns = router.urls
