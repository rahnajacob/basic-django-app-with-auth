from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=50)
    release_year = models.PositiveIntegerField()
    publisher = models.CharField(max_length=40)
    genre = models.CharField(max_length=20)
    personal_rating = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.publisher}, {self.release_year})"

