from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    pass
    
    
class Auction_Listings(models.Model):
    title = models.CharField(max_length=64, blank=False)
    description = models.TextField(max_length= 500, blank=False, null=False)
    starting_bid = models.IntegerField(blank=False)
    image = models.URLField(blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="creator")
    closed = models.BooleanField(default=False)
    winner = models.ForeignKey(User, default=1, on_delete=models.PROTECT, related_name="winner")
    category = models.CharField(blank = False, max_length=64, default='general')
    watchlist = models.ManyToManyField(Watchlist, blank=True, related_name="items")
    

class Comment(models.Model):
    comment = models.TextField(max_length=500, blank=False, null=False)
    item = models.ForeignKey(Auction_Listings, default=1,blank=False, on_delete=models.CASCADE, related_name="comments")
    
