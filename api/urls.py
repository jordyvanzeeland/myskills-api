from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from .views import *
from .components.auth import *
from .components.employment import Employment
from .components.projects import Projects

urlpatterns = [
    path('auth/login', login),
    path('auth/register', register),
    path('employment/', Employment.as_view(), name="employment-list-create"),
    path('employment/<int:pk>', Employment.as_view(), name="employment-detail"),
    path('projects/', Projects.as_view(), name="projects-list-create"),
    path('project/<int:pk>', Projects.as_view(), name="project-detail")
]