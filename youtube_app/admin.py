from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from django.contrib import admin

from youtube_app.models import *

# Register your models here.
class WatchListAdmin(admin.ModelAdmin):
    list_display = ('user', 'video_title')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'order_of_display')


class KeywordResource(resources.ModelResource):

    class Meta:
        model = Keyword
@admin.action(description='Remove videos from most recent')
def remove_recent(modeladmin, request, queryset):
    queryset.update(most_recent='False')

class KeywordResource(resources.ModelResource):
    class Meta:
        model = Keyword
        import_id_fields = ('category',)
        subject = fields.Field(
            column_name='category',
            attribute='category',
            widget=ForeignKeyWidget(Category, 'category'))
class KeywordAdmin(ImportExportModelAdmin):
    list_display = ('id','category', 'keyword', 'channel_id', 'most_recent')
    list_filter = ('most_recent',)
    actions = [remove_recent]
    # resource_class = KeywordResource

class RandomVideoAdmin(admin.ModelAdmin):
    list_display = ('video_id', 'video_title')
class RandomCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'order_of_display')

# class FollowPersonalityAdmin(ImportExportModelAdmin):
#     list_display = ('user', 'keyword')

admin.site.register(WatchList, WatchListAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(AllData)
admin.site.register(FollowPersonality)
admin.site.register(RandomVideo, RandomVideoAdmin)
admin.site.register(RandomCategory, RandomCategoryAdmin)