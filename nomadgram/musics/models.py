from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from nomadgram.users import models as user_models
from taggit.managers import TaggableManager


@python_2_unicode_compatible
class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

@python_2_unicode_compatible
class Music(models.Model):
    title = models.CharField(max_length=50, null=True)
    artist = models.CharField(max_length=50, null=True)
    album_name = models.CharField(max_length=50, null=True)
    album_art = models.ImageField(null=True)
    melon_num = models.IntegerField(null=True,blank=True)
    genie_num = models.IntegerField(null=True,blank=True)
    naver_num = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return '{} - {}'.format(self.title, self.artist)

@python_2_unicode_compatible
class PlayList(TimeStampedModel):
    background_img = models.ImageField(null=True)
    creator = models.ForeignKey(
        user_models.User, null=True, related_name='playlists',on_delete=models.CASCADE)
    tags = TaggableManager()
    caption = models.TextField()
    music_list = models.ManyToManyField(Music)

    def __str__(self):
        return '{} - {}'.format(self.creator, self.caption)