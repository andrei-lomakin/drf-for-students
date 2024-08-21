from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField()
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)

    def __str__(self):
        return self.title
