from django.db import models
from django.contrib.auth.models import User


class Tip(models.Model):
    content = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tip = models.ForeignKey(Tip, on_delete=models.CASCADE, related_name='likes')


class Dislike(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tip = models.ForeignKey(Tip, on_delete=models.CASCADE, related_name='dislikes')