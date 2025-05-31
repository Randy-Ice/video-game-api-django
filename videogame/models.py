import uuid

from django.core.validators import MinLengthValidator
from django.db import models
from django.conf import settings
# Create your models here.


class VideoGame(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(3, message='title should be at least 3 characters long'),
        ]
    )
    description = models.TextField()
    platform = models.ManyToManyField('Platform')
    release_date = models.DateField()
    genre = models.ManyToManyField('Genre')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    AGE_RATING_E = 'E'
    AGE_RATING_TEN_PLUS ='E10+'
    AGE_RATING_TEEN = 'T'
    AGE_RATING_MATURE = 'M'
    AGE_RATING_ADULTS_ONLY ='AO'
    AGE_RATING_PENDING = 'RP'
    AGE_RATING_CHOICES = [
        (AGE_RATING_E, 'E'),
        (AGE_RATING_TEN_PLUS, 'T'),
        (AGE_RATING_TEEN, 'E10+'),
        (AGE_RATING_MATURE, 'M'),
        (AGE_RATING_ADULTS_ONLY, 'AO'),
        (AGE_RATING_PENDING, 'RP'),
    ]
    age_rating = models.CharField(
        max_length=4,
        choices=AGE_RATING_CHOICES,
        default = AGE_RATING_PENDING,
        help_text= 'pick a rating for the game'
    )
    tags = models.ManyToManyField('Tag')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f'{self.title} + release: {self.release_date}'

class Platform(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        unique=True,
        max_length=100,
        validators=[
            MinLengthValidator(3, message='genre should be at least 3 characters long'),
        ]
    )
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    name = models.CharField(
        unique=True,
        max_length=100,
        validators=[
            MinLengthValidator(3, message='name should be at least 3 characters long'),
        ]
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        unique=True,
        max_length=100,
        validators=[
            MinLengthValidator(3, message='name should be at least 3 characters long'),
        ]
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class VideogameImage(models.Model):
    videogame = models.ForeignKey(VideoGame, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='videogame/images')

    def __str__(self):
        return self.videogame.title




class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game = models.ForeignKey(VideoGame, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.game.title} by {self.author}'