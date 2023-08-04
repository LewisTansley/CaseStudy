from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    book_cover = models.ImageField(upload_to='media/default_book_covers/', default='default.png')

    def __str__(self):
        return self.title