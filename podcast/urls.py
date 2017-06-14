from django.conf.urls import url
from .views import *


urlpatterns = [
    # Show list of all shows
    url(r'^$', show_list, name='podcast_shows'),

    # Episode list of one show
    url(r'^(?P<slug>[-\w]+)/$', episode_list, name='podcast_episodes'),

    # Episode list feed by show (RSS 2.0 and iTunes)
    url(r'^(?P<slug>[-\w]+)/feed/$', show_list_feed, name='podcast_feed'),

    # Episode list feed by show (Atom)
    url(r'^(?P<slug>[-\w]+)/atom/$', show_list_atom, name='podcast_atom'),

    # Episode list feed by show (Media RSS)
    url(r'^(?P<slug>[-\w]+)/media/$', show_list_media, name='podcast_media'),

    # Episode sitemap list of one show
    url(r'^(?P<slug>[-\w]+)/sitemap.xml$', episode_sitemap, name='podcast_sitemap'),

    # Episode detail of one show
    url(r'^(?P<show_slug>[-\w]+)/(?P<episode_slug>[-\w]+)/$', episode_detail, name='podcast_episode'),
]
