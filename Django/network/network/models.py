from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="postBY")
    body = models.CharField(max_length = 200)
    time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Post {self.id} by {self.user} at {self.time}"
    
class Followers(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="following")
    followerUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    
    def __str__(self):
        return f"{self.user} is now following {self.followerUser}"
    
class LikeUnlike(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="userlu")
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name="postlu")
    
    def __str__(self):
        return f"{self.user} liked {self.post}"

