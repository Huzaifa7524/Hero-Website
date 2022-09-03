from ast import keyword
from pyexpat import model
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User





# TODO: Must Read!!!!!!!!!!!!
# TODO: If you add another model class then must add this model in settings.py/ADMIN_REORDER to view it in Django Admin section either create a new Group or add in existing one.





# Create your models here.
class WatchList(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    video_title= models.CharField(max_length=300)
    video_description= models.CharField(max_length= 1000)
    video_id= models.CharField(max_length= 20)
    channel_title= models.CharField(max_length=100)
    upload_date=models.CharField(max_length=100)
    channel_profile_pic= models.CharField(max_length=100)
    video_thumbnail_pic= models.CharField(max_length=100)

class Category(models.Model):
    category= models.CharField(max_length=40)
    order_of_display=models.IntegerField(default=0)
    is_random = models.BooleanField(default=False)
    class Meta:
        verbose_name = ("Lane")
        verbose_name_plural = ("Lanes")
    def __str__(self):
        return u'{0}'.format(self.category)

        
class Keyword(models.Model):
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    keyword= models.CharField(max_length=50, null= True, blank=True)
    channel_id= models.CharField(max_length=100, default= '', null= True, blank= True)
    image = models.ImageField(verbose_name='Image',null=True, blank=True, upload_to="upload_images/")
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
# class RandomCategory(models.Model):
    # category_name= models.CharField(max_length=40)
    # order_of_display=models.IntegerField(default=0)
    # def __str__(self):
    #     return u'{0}'.format(self.category_name)

# Add Random Video in Database to show on your page
class RandomVideo(models.Model):
    category= models.ForeignKey(Category,on_delete=models.CASCADE, blank=True, null=True)
    # category= models.ForeignKey(RandomCategory,on_delete=models.CASCADE, blank=True, null=True)
    video_title= models.CharField(max_length=300)
    video_description= models.CharField(max_length= 600)
    video_id= models.CharField(max_length= 20)
    channel_title= models.CharField(verbose_name="Channel Title (Optional) ",max_length=100, null=True, blank=True)
    upload_date=models.CharField( verbose_name="Uploaded Date (Optional) ",max_length=100, null=True, blank=True)
    channel_id= models.CharField(verbose_name="Channel ID (Optional) ",max_length=100, null=True, blank=True)
    video_thumbnail_pic_url= models.URLField(max_length=200, default='', null=True, blank=True)
    video_thumbnail_pic_local = models.ImageField(verbose_name='Thumbnail Image',null=True, blank=True, upload_to="upload_images/")
    class Meta:
        verbose_name = ("Managed Video")
        verbose_name_plural = ("Managed Videos")    

class HeroSection(models.Model):
    video_title= models.CharField(max_length=300 , default='')
    video_description= models.CharField(max_length= 600, default='')
    video_id= models.CharField(max_length= 20, default='')
    channel_title= models.CharField(max_length=100, default='')
    upload_date=models.CharField(max_length=100, default='')
    channel_id= models.CharField(max_length=100, default='')
    background_image_url= models.URLField(max_length=200 , default='')
    class Meta:
        verbose_name = ("Hero Corousel")
        verbose_name_plural = ("Hero Corousels") 
    

  
# Athletes Profile
# 1- Athletes profile categories
class AthleteProfileCategory(models.Model):
    category_name = models.CharField(max_length=300, default='')
    def __str__(self) :
        return str(self.category_name)
    class Meta:
        verbose_name = ("Profile Category")
        verbose_name_plural = ("Profile Categories")

class AthleteProfile(models.Model):
    profile_category= models.ForeignKey(AthleteProfileCategory, on_delete=models.CASCADE, blank=True, null=True)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    avatar_image = models.ImageField(verbose_name='Avatar',null=True, blank=True, upload_to="upload_images/")
    banner_image = models.ImageField(verbose_name='Banner Image',null=True, blank=True, upload_to="upload_images/")
    age = models.IntegerField()
    country = models.CharField(max_length=200)
    experience = models.CharField(max_length=400)
    bio = models.CharField(max_length=500)
    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profile")


    def __str__(self) :
        return str(self.keyword.keyword)

class FollowedAthletes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    followed_athlete = models.ForeignKey(AthleteProfile, on_delete=models.CASCADE)
    class Meta:
        verbose_name = ("Followed Athlete")
        verbose_name_plural = ("Followed Athletes")
    def __str__(self) :
        return str(self.user.username)



