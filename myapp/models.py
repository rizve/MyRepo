from django.db import models
from tinymce.models import HTMLField

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    content = HTMLField()

    def __str__(self):
        return self.title
