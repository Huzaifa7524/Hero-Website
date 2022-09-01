from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from django.contrib import admin

from youtube_app.models import *

# Register your models here.

# *************************************************************************** Watch List

class WatchListResource(resources.ModelResource):

    class Meta:
        model = WatchList

class WatchListAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','user','video_title','video_description','video_id','channel_title','upload_date','channel_profile_pic','video_thumbnail_pic')
    resource_class = WatchListResource

admin.site.register(WatchList, WatchListAdmin)


# *************************************************************************** Random Video


class RandomVideoResource(resources.ModelResource):

    class Meta:
        model = RandomVideo
    

class RandomVideoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','category', 'video_title', 'video_description', 'video_id', 'channel_title', 'upload_date', 'channel_id', 'video_thumbnail_pic_url', 'video_thumbnail_pic_local')

    resource_class = RandomVideoResource


    # ******************** For filtering categories which have is_random field True
    def get_form(self, request, obj=None, **kwargs):
        form = super(RandomVideoAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['category'].queryset = Category.objects.filter(is_random = 'True')
        return form


admin.site.register(RandomVideo, RandomVideoAdmin)


# *************************************************************************** Keywords


# ************* Filter to make most_recent = False for all quersets 

class KeywordResource(resources.ModelResource):
    class Meta:
        model = Keyword
            
class KeywordAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','category', 'keyword', 'channel_id','image', 'most_recent')

    resource_class = KeywordResource

admin.site.register(Keyword, KeywordAdmin)

# *************************************************************************** Hero Selection

class HeroSectionResource(resources.ModelResource):

    class Meta:
        model = HeroSection

class HeroAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','video_title', 'video_description', 'video_id','channel_title', 'upload_date', 'channel_id', 'background_image_url')

    resource_class = HeroSectionResource

    def has_add_permission(self, request):
        base_add_permission = super(HeroAdmin, self).has_add_permission(request)
        if base_add_permission:
            # if there's already an entry, do not allow adding
            count = HeroSection.objects.all().count()
            if count == 0:
                return True
        return False

admin.site.register(HeroSection, HeroAdmin)

# *************************************************************************** Hero Category

class CategoryResource(resources.ModelResource):

    class Meta:
        model = Category


class CategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id', 'category', 'order_of_display', 'is_random')

    resource_class = CategoryResource


admin.site.register(Category,CategoryAdmin)
# *******************************************************************************************************************************************


admin.site.register(AllData)
admin.site.register(FollowPersonality)

# admin.site.register(RandomCategory, RandomCategoryAdmin)

admin.site.register(AthleteProfile)
admin.site.register(AthleteProfileCategory)
admin.site.register(FollowedAthletes)