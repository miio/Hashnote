from django.contrib.syndication.feeds import Feed
from blogs.models import Article,Category

class LatestEntries(Feed):
    title = "Chicagocrime.org site news"
    link = "/sitenews/"
    description = "Updates on changes and additions to chicagocrime.org."

    def items(self):
        return Article.objects.order_by('publish_at')[:5]