from .tasks import hackernews_rss
from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Url)
def notify_subscribers(sender, instance, created, **kwargs):
    if created:
        link_id = instance.id
        link = instance.link
        hackernews_rss(link, link_id)