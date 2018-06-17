from django.contrib import admin

from .models import *

admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Personnel)
admin.site.register(TrackCredit)
admin.site.register(Tag)
