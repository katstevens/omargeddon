from django.contrib import admin

from .models import *


class TrackInline(admin.TabularInline):
    model = Track


class AlbumAdmin(admin.ModelAdmin):
    inlines = [TrackInline]
    list_display = ['title', 'sort_order', 'artist', 'release_date', 'release_label']
    list_editable = ['release_date', 'release_label', 'sort_order']


class TrackCreditInline(admin.TabularInline):
    model = TrackCredit


class TrackAdmin(admin.ModelAdmin):
    inlines = [TrackCreditInline]
    list_display = ['song_title', 'album', 'song_length', 'sort_order']
    list_editable = ['sort_order']


admin.site.register(Album, AlbumAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Personnel)
admin.site.register(TrackCredit)
admin.site.register(Tag)
admin.site.register(SidebarInfo)
