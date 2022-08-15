from import_export import resources
from import_export.admin import ImportExportModelAdmin
from unicodedata import category
from django.contrib import admin

from youtube_app.models import *

# Register your models here.
class WatchListAdmin(admin.ModelAdmin):
    list_display = ('user', 'video_title')


class KeywordResource(resources.ModelResource):

    class Meta:
        model = Keyword
@admin.action(description='Remove videos from most recent')
def remove_recent(modeladmin, request, queryset):
    queryset.update(most_recent='False')
class KeywordAdmin(ImportExportModelAdmin):
    list_display = ('category', 'keyword', 'channel_id', 'most_recent')
    list_filter = ('most_recent',)
    actions = [remove_recent]
# class FollowPersonalityAdmin(ImportExportModelAdmin):
#     list_display = ('user', 'keyword')

admin.site.register(WatchList, WatchListAdmin)
admin.site.register(Category)
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(AllData)
admin.site.register(FollowPersonality)