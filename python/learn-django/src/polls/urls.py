from django.urls import path

from . import views

# Add url patterns here
urlpatterns = [
    path('', views.index, name='index'),
]
