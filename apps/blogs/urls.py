from django.urls import path

from apps.blogs.views import index

urlpatterns = [
    path('', index, name='homepage'),
]