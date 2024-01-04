from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
from .models import User, Post, Followers, LikeUnlike
from django.db.models import Count


def index(request):
    allPosts = Post.objects.all().order_by("id").reverse()
    paginator = Paginator(allPosts, 10)
    pageNumber = request.GET.get("page")
    showedPosts = paginator.get_page(pageNumber)
    
    likes = LikeUnlike.objects.all()
    likedPosts = []
    try:
        for like in likes:
            if like.user.id == request.user.id:
                likedPosts.append(like.post.id)
    except:
        likedPosts= []
    return render(request, "network/index.html", {"allPosts": allPosts, "showedPosts": showedPosts, "likedPosts": likedPosts})

def myPost(request):
    if request.method == "POST":
        post = Post()
        post.user = User.objects.get(pk=request.user.id)
        post.body = request.POST["postBody"]
        post.save()
        return HttpResponseRedirect(reverse(index))
    
def profile(request, id):
    user = User.objects.get(pk=id)
    allPosts = Post.objects.filter(user=user).order_by("id").reverse()  # Filtrar posts pelo usuário
    following = Followers.objects.filter(user=user)
    followers = Followers.objects.filter(followerUser = user)
    
    try:
        follow = followers.filter(user=User.objects.get(pk=request.user.id))
        if len(follow) !=0:
            isFollowing = True
        else:
            isFollowing = False
    except:
        isFollowing = False
        
    paginator = Paginator(allPosts, 10)
    pageNumber = request.GET.get("page")
    showedPosts = paginator.get_page(pageNumber)
    likes = LikeUnlike.objects.all()
    likedPosts = []
    try:
        for like in likes:
            if like.user.id == request.user.id:
                likedPosts.append(like.post.id)
    except:
        likedPosts= []
    return render(request, "network/profile.html", {"allPosts": allPosts, "showedPosts": showedPosts, "following": following, "followers": followers, "isFollowing": isFollowing, "uProfile": user, "likedPosts": likedPosts})

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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
    
def follow(request):
    result = request.POST["followinput"]
    followData = User.objects.get(username=result)
    followers = Followers(user = User.objects.get(pk=request.user.id), followerUser = followData)
    followers.save()
    id = followData.id
    return HttpResponseRedirect(reverse(profile, kwargs={"id": id}))    


def unfollow(request):
    result = request.POST["followinput"]
    followData = User.objects.get(username=result)
    followers = Followers.objects.filter(user=User.objects.get(pk=request.user.id), followerUser=followData)
    followers.delete()
    id = followData.id
    return HttpResponseRedirect(reverse(profile, kwargs={"id": id}))    


def following(request):
    user = User.objects.get(pk = request.user.id)
    followingUser = Followers.objects.filter(user = user)
    posts = Post.objects.all().order_by("id").reverse()
    followingPosts = []
    
    for post in posts:
        for followingU in followingUser:
            if followingU.followerUser == post.user:
                followingPosts.append(post)
    
    paginator = Paginator(followingPosts, 10)
    pageNumber = request.GET.get("page")
    showedPosts = paginator.get_page(pageNumber)
    likes = LikeUnlike.objects.all()
    likedPosts = []
    try:
        for like in likes:
            if like.user.id == request.user.id:
                likedPosts.append(like.post.id)
    except:
        likedPosts= []
    return render(request, "network/followingposts.html", {"showedPosts": followingPosts,"likedPosts": likedPosts})

                
def edit(request, postid):
    if request.method == "POST":
        data = json.loads(request.body)
        editPost = Post.objects.get(pk=postid)
        editPost.body = data["content"]
        editPost.save()
        return JsonResponse({"answer": "Edited!", "data": data["content"]})
    
def like(request, postid):
    post = Post.objects.get(pk=postid)
    user = User.objects.get(pk=request.user.id)
    existingLike = LikeUnlike.objects.filter(user=user, post=post)
    if not existingLike:
        newLike = LikeUnlike(user=user, post=post)
        newLike.save()
    likes = post.postlu.count()
    return JsonResponse({"likes": likes})

def unlike(request, postid):
    post = Post.objects.get(pk=postid)
    user = User.objects.get(pk=request.user.id)
    notLike = LikeUnlike.objects.filter(user=user, post=post)
    notLike.delete()
    likes = post.postlu.count()
    return JsonResponse({"likes": likes})
