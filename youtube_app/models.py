from ast import keyword
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class WatchList(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    video_title= models.CharField(max_length=300)
    video_description= models.CharField(max_length= 600)
    video_id= models.CharField(max_length= 20)
    channel_title= models.CharField(max_length=100)
    upload_date=models.CharField(max_length=100)
    channel_profile_pic= models.CharField(max_length=100)
    video_thumbnail_pic= models.CharField(max_length=100)

class Category(models.Model):
    category= models.CharField(max_length=40)
    def __str__(self):
        return str(self.category)
class Keyword(models.Model):
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    keyword= models.CharField(max_length=50, null= True, blank=True)
    channel_id= models.CharField(max_length=100, default= '', null= True, blank= True)
    data=models.JSONField(null= True, blank=True)
    most_recent= models.BooleanField(default=False)
    def __str__(self):
        return u'{0}'.format(self.keyword)

class AllData(models.Model):
    data= models.JSONField(null=True, blank=True)


class FollowPersonality(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    keyword= models.ForeignKey(Keyword, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.keyword.keyword)
    def __str__(self):
        return "{0}".format(self.keyword.keyword)

  




