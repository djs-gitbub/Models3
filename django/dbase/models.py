from django.db import models

class Vocab(models.Model):
    author = models.CharField(max_length = 100, unique = False)
    title = models.CharField(max_length = 100, unique = False)
    year = models.IntegerField(unique = False)
    genre = models.CharField(max_length = 100, unique = False)