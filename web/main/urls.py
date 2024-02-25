# urls.py

from django.urls import path
from . import views
from .views import get_lastfm_track 

urlpatterns = [
    path('', views.index),
    path('music', views.music),
    path('api/music-data/', get_lastfm_track, name='music-data'),
]
