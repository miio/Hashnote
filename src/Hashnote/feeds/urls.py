from django.conf.urls.defaults import *

from django.contrib import admin
from feeds import LatestEntries


admin.autodiscover()

feeds = {
    'latest': LatestEntries,
    'categories': LatestEntries,
}

urlpatterns = patterns('',
    url(r'^(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
)
