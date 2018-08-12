from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=100)
    tag_slug = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_name


class Album(models.Model):
    title = models.CharField(max_length=256)
    artist = models.CharField(default="Omar Rodriguez Lopez", max_length=256)
    description = models.TextField(null=True, blank=True)
    image_file = models.ImageField(null=True, blank=True, upload_to="images/albums")
    image_path = models.CharField(null=True, blank=True, max_length=256)
    release_date = models.CharField(max_length=100)
    release_label = models.CharField(max_length=100, default="Rodriguez Lopez Productions")
    sort_order = models.IntegerField(default=0)

    tags = models.ManyToManyField(Tag, related_name='album_tags', blank=True)

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return self.title

    def tracklisting(self):
        return self.track_set.all()

class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=256)
    song_length = models.CharField(max_length=50, null=True, blank=True)
    sort_order = models.IntegerField(default=0)

    tags = models.ManyToManyField(Tag, related_name='track_tags', blank=True)

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return self.song_title

    def contributors(self):
        return self.trackcredit_set.all()

class Personnel(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Personnel'

    def __str__(self):
        return self.name


class TrackCredit(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    credit = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.track.album.title, self.contributor.name)
