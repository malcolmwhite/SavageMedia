from django.db import models
from django.contrib.auth.models import User


class Campaign(models.Model):
    name = models.TextField
    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField
    accounts_liked = models.ManyToManyField(SocialMediaAccount)


class SearchTarget(models.Model):
    campaigns = models.ManyToManyField(Campaign)
    services = models.ManyToManyField(SocialMediaService)

    class Meta:
        abstract = True


class TargetPhrase(SearchTarget):
    phrase = models.TextField


class TargetGraph(SearchTarget):
    central_user = models.TextField
    depth = models.IntegerField


class SocialMediaService(models.Model):
    name = models.TextField
    icon = models.ImageField
    post_name = models.TextField


class SocialMediaAccount(models.Model):
    handle = models.TextField
    service = models.ForeignKey(SocialMediaService)


class FlightDate(models.Model):
    start = models.DateTimeField
    end = models.DateTimeField
    campaign = models.ForeignKey(Campaign)
