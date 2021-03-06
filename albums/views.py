from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Album, Tag, Track, SidebarInfo

def _sidebar():
    # TODO: make this a global context and cache it
    return SidebarInfo.objects.filter(visible=True)

def index(request):
    # TODO: pagination
    albums = get_list_or_404(Album)
    return render(request, 'albums.html', context={'albums': albums, 'sidebar': _sidebar()})


def about(request):
    return render(request, 'about.html', context={'sidebar': _sidebar()})


def playlists(request):
    return render(request, 'playlists.html', context={'sidebar': _sidebar()})


def single_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)

    personnel = []
    for track in album.tracklisting():
        track_contributors = track.contributors()
        for credit in track_contributors:
            if credit.contributor not in personnel:
                personnel.append(credit.contributor)

    return render(request, 'single_album.html', context={'album': album, 'contributors': personnel, 'sidebar': _sidebar()})


def single_track(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    return render(request, 'tracks.html', context={'tracks': [track], 'sidebar': _sidebar()})


def albums_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, tag_slug=tag_slug)
    albums = get_list_or_404(Album, tags=tag)
    return render(request, 'albums.html', context={'albums': albums, 'sidebar': _sidebar()})


def tracks_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, tag_slug=tag_slug)
    tracks = get_list_or_404(Track, tags=tag)
    return render(request, 'tracks.html', context={'tracks': tracks, 'sidebar': _sidebar()})
