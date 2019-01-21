from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
from rest_framework.permissions import AllowAny

class MusicDetail(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, music_id, format=None):
        user = request.user
        try:
            music = models.Music.objects.get(id=music_id)
        except models.Music.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.MusicInfoSerializer(music, context={'request': request})

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class PlayListDetail(APIView):
    permission_classes = (AllowAny,)
    def find_own_playlist(self, list_id, user):
        try:
            play_list = models.PlayList.objects.get(id=list_id, creator=user)
            return play_list
        except models.PlayList.DoesNotExist:
            return None

    permission_classes = (AllowAny,)
    def get(self, request, list_id, format=None):
        user = request.user
        try:
            play_list = models.PlayList.objects.get(id=list_id)
        except models.PlayList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.PlayListSerializer(play_list, context={'request': request})

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class SearchByID(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):

        userid = request.query_params.get('userid', None)
        
        if userid is not None:
            try:
                play_list = models.PlayList.objects.filter(
                    creator=userid).distinct()
            except models.PlayList.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = serializers.PlayListSerializer(play_list, context={'request': request},many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)


class SearchBytags(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):

        hashtags = request.query_params.get('hashtags', None)
        if hashtags is not None:
            hashtags = hashtags.split(",")
            
            play_list = models.PlayList.objects.filter(
                tags__name__in=hashtags).distinct()

            serializer = serializers.PlayListSerializer(play_list,  context={'request': request}, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)
