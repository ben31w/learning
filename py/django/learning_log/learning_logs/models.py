"""
models.py is created whenever you create an app in Django
(in Django, a project is composed of individual apps that work together).

models.py defines the data we want to manage in our app.

To use our models, we have to tell Django to include our app in the overall project.
Go the project's settings.py and add this app (learning_logs) to the
INSTALLED_APPS list.Models extend the models.Model class

In the Learning Log, we want to manage topics and entries.
Each entry will be tied to a topic and has a timestamp.
"""

from django.contrib.auth.models import User
from django.db import models


# Create your models here
class Topic(models.Model):
    """
    Topic model. A topic that the user can use to organize their entries.

    Topic should store a name, timestamp of when it is added, and the user who
    created the topic.
    """
    # models.SomeField are the fields that Django will create in the database.
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Entry(models.Model):
    """
    Entry model. An entry is something specific learned about a topic.

    Entry should have text and a timestamp of when it is added. Cascade deletion:
    when a topic is deleted, so are all entries associated with it.
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text) >= 50:
            return f"{self.text[:50]}..."
        return self.text

