from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auction_Listings(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    starting_bid = models.IntegerField()
    image = models.URLField(default="https://banner2.cleanpng.com/20180409/zrq/kisspng-post-it-note-paper-link-free-sticky-notes-clip-art-post-it-5acbacab077577.2543104915232974510306.jpg")