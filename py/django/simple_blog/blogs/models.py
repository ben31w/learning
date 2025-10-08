from django.db import models


# Create your models here.
class BlogPost(models.Model):
    """A simple blog post with a title and text."""
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

