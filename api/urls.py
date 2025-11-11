from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from .views import *
from .components.auth import *

urlpatterns = [
    path('auth/login', login),
    path('auth/register', register),
]