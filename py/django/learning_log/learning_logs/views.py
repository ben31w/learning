"""
views.py is created for each app you make.

A view function takes an HTTP request and returns an HTTP response (like an
HTML page, a redirect, a 404 error, an XML doc, an image)

Views can contain logic needed to properly generate the HTTP response. In this
example, it simply calls render() without any additional logic.

For most pages, we want to restrict access unless the user is logged in.
So we use the @login_required decoration to redirect the user to the login page
if they access certain pages while not logged in.
"""
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import EntryForm, TopicForm
from .models import Entry, Topic


# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """A page that lists all the user's topics."""
    # Get list of ordered topics. Create a context dictionary so
    #  the topics can be rendered on topics.html. In the context dictionary,
    #  the key is the variable we use to refer to the data in the response

    # Users should only be able to view their topics, not other users'
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """
    A page that lists a single topic and all its entries.
    :param request: HTTP request (boilerplate)
    :param topic_id: value captured by expression .../<int:topic_id>/ in URL
    :return: page about a single topic
    """
    topic = Topic.objects.get(id=topic_id)
    verify_topic_owner(topic.owner, request.user)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """"A page where users can enter a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TopicForm()
    else:
        # POST data submitted; process data
        # save() writes data from form to the database
        form = TopicForm(data=request.POST)
        if form.is_valid():
            this_topic = form.save(commit=False)
            this_topic.owner = request.user
            this_topic.save()
            return redirect('learning_logs:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """A page where users can add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    verify_topic_owner(topic.owner, request.user)

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = EntryForm()
    else:
        # POST data submitted; process data
        # save(commit=False) creates an object without saving it the db yet.
        #  (we need to assign the topic first)
        form = EntryForm(data=request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.topic = topic
            entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """A page where users can edit an entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    verify_topic_owner(topic.owner, request.user)

    if request.method != 'POST':
        # No data submitted; this is the initial request.
        #  instance=entry initializes the form prefilled with info from the
        #  existing entry
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data
        # instance=entry initiliaes the form with info from the existing entry,
        #  but data=request.POST accounts for the user's updates
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


def verify_topic_owner(owner, user):
    """
    Verify that the user is accessing a topic that they own. If not,
    raise a 404 error (page could not be found)
    """
    if owner != user:
        raise Http404

