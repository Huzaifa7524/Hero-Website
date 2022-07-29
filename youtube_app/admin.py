from django.contrib import admin

from youtube_app.models import WatchList

# Register your models here.
class WatchListAdmin(admin.ModelAdmin):
    list_display = ('user', 'video_title')

admin.site.register(WatchList, WatchListAdmin)