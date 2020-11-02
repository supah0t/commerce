from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    watchlist = models.ManyToManyField('Auction_Listings', blank=True, related_name="person")
    
#class TimeStamp(models.Model):
#    created_at = models.DateTimeField(auto_now_add=True)
#    updated_at = models.DateTimeField(auto_now=True)
#    class Meta:
#        abstract = True
    
class Auction_Listings(models.Model):
    title = models.CharField(max_length=64, blank=False)
    description = models.TextField(max_length= 500, blank=False, null=False)
    starting_bid = models.IntegerField(blank=False)
    image = models.URLField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    closed = models.BooleanField(default=False)
    winner = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT, related_name="itemWon")
    category = models.CharField(blank = False, max_length=64, default='general'),

    

class Comment(models.Model):
    comment = models.TextField(max_length=500, blank=False, null=False)
    item = models.ForeignKey(Auction_Listings, blank=False, on_delete=models.CASCADE, related_name="comments")
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="poster")