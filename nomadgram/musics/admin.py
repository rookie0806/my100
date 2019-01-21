from django.contrib import admin
from . import models


@admin.register(models.Music)
class MusicAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'artist',
        'album_name',
        'album_art'
    )

@admin.register(models.PlayList)
class PlayListAdmin(admin.ModelAdmin):

    list_display = (
        'creator',
        'caption',
        'background_img'
    )
