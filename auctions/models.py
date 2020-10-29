from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Auction_Listings(models.Model):
    title = models.CharField(max_length=64, blank=False)
    description = models.TextField(max_length= 500, blank=False, null=False)
    starting_bid = models.IntegerField(blank=False)
    image = models.URLField(blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="creator")
    closed = models.BooleanField(default=False)
    winner = models.ForeignKey(User, default=1, on_delete=models.PROTECT, related_name="winner")