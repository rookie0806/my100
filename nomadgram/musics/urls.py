from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^music/(?P<music_id>[0-9]+)/$',
        view=views.MusicDetail.as_view(),
        name='music_detail'
    ),
    url(
        regex=r'^list/(?P<list_id>[0-9]+)/$',
        view=views.PlayListDetail.as_view(),
        name='playlist_detail'
    ),
    url(
        regex=r'^searchbyid/$',
        view=views.SearchByID.as_view(),
        name='IDList'
    ),
    url(
        regex=r'^searchbytag/$',
        view=views.SearchBytags.as_view(),
        name='tagList'
    ),
]
