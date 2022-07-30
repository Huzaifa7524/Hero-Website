from atexit import register
from django import template
from youtube_app.models import WatchList, Category, Keyword
register= template.Library()
@register.filter(name='VideoCategory')
def VideoCategory(string_value):
    all_keywords= Keyword.objects.all()
    print('String#######', string_value)
    list=[]
    for keyword in all_keywords:
        print('keyword#######', keyword.keyword)
        if keyword.keyword in string_value:
            print('if temp')
            return keyword.category.category
        else:
            pass