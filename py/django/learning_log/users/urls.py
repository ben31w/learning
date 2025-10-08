"""Define URL patterns for users app"""

from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    # Include default auth URLs. These include URL patters like login and logout
    #  ex: .../users/login/
    #  This is tied to a default view function called users:login, which loads
    #  the template learning_log/users/templates/registration/login.html
    path('', include('django.contrib.auth.urls')),
    # Registration page
    path('register/', views.register_user, name='register'),
]
