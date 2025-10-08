from django.shortcuts import render

from .forms import AutoForm


# Create your views here.
def index(request):
    """home page"""
    form = AutoForm()
    return render(request, 'demo/index.html', {'form': form})
