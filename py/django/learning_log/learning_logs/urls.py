"""Define URL patterns for the app learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'


# List of URL mappings for the app learning_log.
# i.e., list of pages that can be requested

# path() takes what goes after the base URL, the function to call, and
#  a name to refer to this path in other code sections.
urlpatterns = [
    # Home page:
    path('', views.index, name='index'),
    # Topics page:
    path('topics/', views.topics, name='topics'),
    # Detail page with list of entries for a single topic (store the int in a
    #   variable called topic_id, which is passed to views.topic):
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic:
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry to a topic:
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for edting an entry:
    path('edit_entry<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
