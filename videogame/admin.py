from django.contrib import admin
from .models import (VideoGame, Platform, Publisher,
                     Genre, Tag, Category, VideogameImage, Post)


# Register your models here.
admin.site.register(VideoGame)
admin.site.register(VideogameImage)
admin.site.register(Platform)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post)
