from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    itemCategory = models.CharField(max_length=30)

    def __str__(self):
        return self.itemCategory


class Bids(models.Model):
    bidOwner = models.ForeignKey(User, on_delete= models.CASCADE, blank=True, null=True, related_name="ownerBid")
    bid = models.FloatField(default=0)

    def __str__(self):
        return str(self.bid)

class Auction(models.Model):
    itemName = models.CharField(max_length=100)
    ownerUser = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    activeAuction = models.BooleanField(default=True)
    itemCategory = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    description = models.CharField(max_length=500)
    itemImage = models.CharField(max_length=1000)#URL
    startBid = models.ForeignKey(Bids, on_delete=models.CASCADE, blank=True, null=True, related_name="initialBid")
    watchlist = models.ManyToManyField(User, blank=True, related_name="userWatchlist")

    def __str__(self):
        return self.itemName



class Comments(models.Model):
    commentOwner = models.ForeignKey(User, on_delete= models.CASCADE, blank=True, null=True, related_name="ownerComment")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, blank=True, null=True, related_name="auctionComment")
    message = models.CharField(max_length=300, default="")

    def __str__(self):
        return f'{self.commentOwner} comments on {self.auction}'