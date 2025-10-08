"""
admin.py is created when you create an app.

This is where you register the models you create in models.py
"""

from django.contrib import admin

from .models import Topic, Entry

# Register your models here
admin.site.register(Topic)
admin.site.register(Entry)
