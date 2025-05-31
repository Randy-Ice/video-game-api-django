from django.urls import path
from rest_framework.routers import DefaultRouter
from videogame.views import VideogameViewSet

router = DefaultRouter()
router.register('videogames', VideogameViewSet)
urlpatterns = router.urls
