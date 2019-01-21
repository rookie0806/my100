from rest_framework import serializers
from . import models
from rest_framework import serializers
from nomadgram.users import models as user_models
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class MusicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Music
        fields = (
            'title',
            'artist',
            'album_name',
            'album_art',
            'melon_num',
            'genie_num',
            'naver_num',
        )

class PlayListSerializer(serializers.ModelSerializer):
    music_list = MusicInfoSerializer(many=True)
    tags = TagListSerializerField()
    class Meta:
        model = models.PlayList
        fields = (
            'creator',
            'caption',
            'background_img',
            'music_list',
            'tags',
            'created_at',
            'updated_at'
        )




