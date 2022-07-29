from unicodedata import category
from django.contrib import admin

from youtube_app.models import *

# Register your models here.
class WatchListAdmin(admin.ModelAdmin):
    list_display = ('user', 'video_title')



class KeywordAdmin(admin.ModelAdmin):
    list_display = ('category', 'keyword')

admin.site.register(WatchList, WatchListAdmin)
admin.site.register(Category)
admin.site.register(Keyword, KeywordAdmin)