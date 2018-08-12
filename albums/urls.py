"""omargeddon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='album_index'),
    path('albums/<int:album_id>', views.single_album, name='single_album'),
    path('albums/tag/<str:tag_slug>', views.albums_by_tag, name='albums_by_tag'),
    path('tracks/tag/<str:tag_slug>', views.tracks_by_tag, name='tracks_by_tag'),
    path('tracks/<int:track_id>', views.single_track, name='single_track'),
    path('playlists', views.playlists, name='playlists'),
    path('about', views.about, name='about'),
]
