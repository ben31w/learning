from django.shortcuts import render

from .models import Pizza, Topping


# Create your views here.
def index(request):
    """Home page"""
    return render(request, 'pizzas/index.html')


def menu(request):
    """Menu page"""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/menu.html', context)

