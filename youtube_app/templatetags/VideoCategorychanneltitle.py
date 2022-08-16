from atexit import register
from django import template
from youtube_app.models import WatchList, Category, Keyword
register= template.Library()
@register.filter(name='VideoCategorychanneltitle')
def VideoCategorychanneltitle(string_value):
    all_keywords= Keyword.objects.all()
    
    list=[]
    for keyword in all_keywords:
        # print('Channel filter#######', keyword.keyword)
        if keyword.keyword == string_value or keyword.keyword in string_value:
            # print('String####### channel', string_value, keyword.channel_id)
            # print('if temp video channel', keyword.category.category)
            return keyword.category.category
        
        else:
            # print('else')
            pass
            
            