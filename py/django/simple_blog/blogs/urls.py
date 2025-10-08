"""URL mappings for blogs app"""

from django.contrib import admin
from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('create-blog/', views.create_blog, name='create_blog'),
]
