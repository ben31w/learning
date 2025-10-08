from django.shortcuts import redirect, render

from .forms import BlogForm
from .models import BlogPost


# Create your views here.
def index(request):
    """Home page where users can view and create blogs"""
    blogs = BlogPost.objects.order_by('-date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/index.html', context)


def create_blog(request):
    """A page for creating blogs"""
    if request.method != 'POST':
        # No data submitted; load blank form
        form = BlogForm()
    else:
        # Data submitted; validate it and save to database, or reject it.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'form': form}
    return render(request, 'blogs/create_blog.html', context)

