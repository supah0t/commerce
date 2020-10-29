from django.contrib import admin

from .models import Auction_Listings, User

# Register your models here.
admin.site.register(Auction_Listings)
admin.site.register(User)