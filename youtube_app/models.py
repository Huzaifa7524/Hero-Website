from ast import keyword
from pyexpat import model
from unicodedata import category
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
    order_of_display=models.IntegerField(default=0)
    def __str__(self):
        return u'{0}'.format(self.category)
class Keyword(models.Model):
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    keyword= models.CharField(max_length=50, null= True, blank=True)
    channel_id= models.CharField(max_length=100, default= '', null= True, blank= True)
    data=models.JSONField(null= True, blank=True)
    most_recent= models.BooleanField(default=True)
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

# Random categories
class RandomCategory(models.Model):
    category_name= models.CharField(max_length=40)
    order_of_display=models.IntegerField(default=0)
    def __str__(self):
        return u'{0}'.format(self.category_name)

# Add Random Video in Database to show on your page
class RandomVideo(models.Model):
    category= models.ForeignKey(RandomCategory,on_delete=models.CASCADE, blank=True, null=True)
    video_title= models.CharField(max_length=300)
    video_description= models.CharField(max_length= 600)
    video_id= models.CharField(max_length= 20)
    channel_title= models.CharField(max_length=100)
    upload_date=models.CharField(max_length=100)
    channel_id= models.CharField(max_length=100)
    video_thumbnail_pic_url= models.URLField(max_length=200, default='')

class HeroSection(models.Model):
    background_image_url= models.URLField(max_length=200)
    

  




