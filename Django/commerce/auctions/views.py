from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Auction, Comments, Bids


def index(request):
    auctionlist = Auction.objects.filter(activeAuction = True)
    categories = Category.objects.all()
    return render(request, "auctions/index.html", {"list": auctionlist, "categories": categories})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def createAuction(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "auctions/createauction.html", {"categories": categories})
    else:
        user = request.user
        bid = Bids()
        bid.bid = request.POST["startBid"]
        bid.bidOwner = None
        bid.save()
        a = Auction()
        a.itemName = request.POST["itemName"]
        a.itemCategory = Category.objects.get(itemCategory = request.POST["category"])
        a.description = request.POST["description"]
        a.itemImage = request.POST["itemImage"]
        a.startBid = bid
        a.ownerUser = user
        a.save()
        return HttpResponseRedirect(reverse("index"))
    
def searchByCategory(request):
    if request.method == "POST":
        receivedCategory = request.POST["category"]
        category = Category.objects.get(itemCategory = receivedCategory)
        auctionlist = Auction.objects.filter(activeAuction = True, itemCategory = category)
        categories = Category.objects.all()
        return render(request, "auctions/index.html", {"list": auctionlist, "categories": categories})
    
def auction(request,id):
    auctionList = Auction.objects.get(pk=id)
    onWatchlist = request.user in auctionList.watchlist.all()
    comments = Comments.objects.filter(auction=auctionList)
    return render(request, "auctions/auction.html", {"itemAuction": auctionList, "onWatchlist": onWatchlist, "comments": comments, "isOwner": request.user.username == auctionList.ownerUser.username})

def removeFromWatchlist(request, id):
    auctionList = Auction.objects.get(pk=id)
    user = request.user
    auctionList.watchlist.remove(user)
    return HttpResponseRedirect(reverse("auction", args=(id, )))


def addFromWatchlist(request, id):
    auctionList = Auction.objects.get(pk=id)
    user = request.user
    auctionList.watchlist.add(user)
    return HttpResponseRedirect(reverse("auction", args=(id, )))

def showWatchList(request):
    user = request.user
    watchlist = user.userWatchlist.all()
    return render(request, "auctions/watchlist.html", {"list": watchlist})

def sendComment(request, id):
    user = request.user
    myauction = Auction.objects.get(pk=id)
    mycomment = request.POST.get("comment")
    comment = Comments()
    comment.commentOwner = user
    comment.auction = myauction
    comment.message = mycomment
    comment.save()
    return HttpResponseRedirect(reverse("auction", args=(id, )))

def sendBid(request, id):
    bid = float(request.POST["setBid"])
    auction = Auction.objects.get(pk=id)
    onWatchlist = request.user in auction.watchlist.all()
    comments = Comments.objects.filter(auction=auction)
    if bid > auction.startBid.bid:
        newBid = Bids()
        newBid.bid = bid
        newBid.bidOwner = request.user
        newBid.save()
        auction.startBid = newBid
        auction.save()
        return render(request, "auctions/auction.html", {"itemAuction": auction, "isNewBid":True,"resultMessage": "Congratulations! You have the highest bid at moment!", "onWatchlist": onWatchlist, "comments": comments, "isOwner": request.user.username == auction.ownerUser.username})
    else:
        return render(request, "auctions/auction.html", {"itemAuction": auction,"isNewBid":False ,"resultMessage": "Sorry, your bid is lower than the actual bid! Please try again!", "onWatchlist": onWatchlist, "comments": comments, "isOwner": request.user.username == auction.ownerUser.username})

def endAuction(request, id):
    auctions = Auction.objects.get(pk=id)
    auctions.activeAuction = False
    auctions.save()
    onWatchlist = request.user in auctions.watchlist.all()
    comments = Comments.objects.filter(auction=auctions)
    return render(request, "auctions/auction.html", {"itemAuction": auctions, "isNewBid":True, "resultMessage": "Your auction ended!", "onWatchlist": onWatchlist, "comments": comments, "isOwner": request.user.username == auctions.ownerUser.username})
