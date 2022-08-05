from multiprocessing import context
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render,redirect

from .models import *
from googleapiclient.discovery import build
from django.contrib.auth.models import User
import datetime
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.core.paginator import Paginator


# Youtube API Key
api_key= 'AIzaSyAzaAIFiU2QKcD4sqC47j-I9-0fAk3awHw'
api_key_2='AIzaSyAo9njxj8OJpWshmpCyamYf9GJXN-kIi64'
api_key_3='AIzaSyBztkmRfxkYWS9QCtS9XD8r6clecRBVK2s'
api_key_4='AIzaSyA4Mt5QJqtcTJ77BHIeFAj12M6s5mSUiFQ'
api_key_5='AIzaSyA6aQiZykCZBYzGheYaKYdJYPKUsAQrrCs'

youtube = build('youtube', 'v3', developerKey=api_key)
# Create your views here.
def register(request):
    if request.method== 'POST':
        fullname= request.POST.get('name')
        username= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('password')
        if User.objects.filter(username=username):
            return redirect('/register')
        user_obj= User(username=username, email=email, first_name= fullname) 
        user_obj.set_password(password)
        user_obj.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        
        return redirect('/home')
    return render(request, 'users/register.html')
def loginUser(request):
        if request.user.is_authenticated:
            return redirect('/home')
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            try:
                user = User.objects.get(username=username)
            except:
                 return redirect('/')
            if user:

                username = user.username
                user = authenticate(request, username=username, password=password) # check password

            if user is not None:
                login(request, user)
                return redirect('/home')	
            
        return render(request,'users/login.html',)

def logoutUser(request):
        print('1212122')
        logout(request)
        return redirect('/')


def home(request):
    data_list=[]
    paginator_list=[]
    paginator_list_2=[]
    # all_data_obj=AllData.objects.get(id=1)
    categories= Category.objects.all()
    index=0
    for category in categories:
        try:
            keyword_obj= Keyword.objects.filter(category__category=category)
            
            paginator = Paginator(keyword_obj, 2)
            page = request.GET.get('page', 1)
            keywords = paginator.get_page(page)
            for key in keywords:
                paginator_list = paginator_list+ key.data
            obj_1=keyword_obj[0]
            # obj_2=keyword_obj[1]
            # print('keyword obj',obj_2)
        
            data_list= data_list+obj_1.data
            # data_list= data_list+obj_2.data
            
            index+=1
        except:
            pass
    print('Paginator', paginator_list)
    # all_data_obj=Keyword.objects.get(id=1)
    # data_list=data_list+all_data_obj.data
    # data_list= data_list+video_items
    # print(video_items)
    
    watchlist_videos= WatchList.objects.filter(user=request.user)
    videos_id_list=[]
    for video in watchlist_videos:
        videos_id_list.append(video.video_id)

    
    # print(video_response)
    context= {'data': paginator_list, 'watchlist_videos': videos_id_list, 'categories':categories, 'keywords_page_info':keywords}
    return render(request, 'youtube/home.html', context)

# AJAX Call to get data of remaining Objects
@csrf_exempt
def home_data_ajax(request):
    if request.method == "POST":
        print('post req')
        page_number= request.POST.get('page_number') 
        next_page= int(page_number)+1
        category_name= request.POST.get('category_name') 
        print('page_number',page_number)
        print('next_page',next_page)
        print('category_name',category_name)
        keyword_obj= Keyword.objects.filter(category__category=category_name )
        
        paginator = Paginator(keyword_obj, 2)
        page = request.GET.get('page', next_page)
        keywords = paginator.get_page(page)
        paginator_list=[]
        for key in keywords:
            paginator_list = paginator_list+ key.data
        return JsonResponse({'data': paginator_list, 'page_number': next_page})
        

def dummy_home(request):
    # api_key = '#YOURAPIKEY'

   

    # request1 = youtube.channels().list(
    #         part='contentDetails',
    #         forUsername='schafer5'
    #     )
    # request_channel_snippet = youtube.channels().list(
    #         part='snippet',
    #         forUsername='schafer5' 
    #     )

    # response = request1.execute()
    # response_channel_snippet=request_channel_snippet.execute()
    # # print('response****************',response)
    # items=response['items']
    # snippet_items= response_channel_snippet['items']
    # snippet_item= snippet_items[0]
    # profile_picture= snippet_item['snippet']['thumbnails']['default']['url']

    # item=items[0]
    # content= item['contentDetails']
    # playlist= content['relatedPlaylists']
    # uploads=playlist['uploads']
    # print(response)
    # print(uploads)
    # all_keywords= Keyword.objects.all()
    keyword_var=''
    data_list= []   
    all_keywords_updated= Keyword.objects.all() 
    for keyword in all_keywords_updated:
        data_list=data_list+keyword.data
        # data_list= data_list+video_items
    # print(video_items)
    
    watchlist_videos= WatchList.objects.filter(user=request.user)
    videos_id_list=[]
    for video in watchlist_videos:
        videos_id_list.append(video.video_id)

    categories= Category.objects.all
    # print(video_response)
    context= {'data': data_list, 'watchlist_videos': videos_id_list, 'categories':categories}
    return render(request, 'youtube/home.html', context)

def video_view(request):
    
  
    if request.method == 'POST':
        video_description= request.POST.get('video_description')
        video_title= request.POST.get('video_title')
        video_id= request.POST.get('video_id')
        channel_title= request.POST.get('channel_title')
        channel_profile= request.POST.get('channel_id')
        print('channel_id', channel_profile)
        # To get the cahnnel profile pic
        request_channel_snippet = youtube.channels().list(
            part='snippet',
            id=channel_profile 
        )
        response_channel_snippet=request_channel_snippet.execute()
        snippet_items= response_channel_snippet['items']
        snippet_item= snippet_items[0]
        profile_picture= snippet_item['snippet']['thumbnails']['default']['url']
        # End profile picture
        video_date= request.POST.get('video_date')
        d1 = datetime.datetime.strptime(video_date,"%Y-%m-%dT%H:%M:%SZ")
        # now = date.now()
        # d2 = datetime.datetime.strptime(now,"%Y-%m-%dT%H:%M:%SZ")


        print('dq****', d1)
        new_format = "%Y-%m-%d"
        upload_date=(d1.strftime(new_format))
    context = {'video_description': video_description, 'video_title': video_title, 'video_id': video_id, 'channel_title': channel_title, 'channel_profile': profile_picture, 'upload_date': d1}
    return render(request, 'youtube/video_player.html', context)

@csrf_exempt
def add_to_watchlist(request):
    # if request.is_ajax():
    if request.method == 'POST':
        video_description = request.POST.get('video_description')
        video_title = request.POST.get('video_title')
        video_id = request.POST.get('video_id')
        channel_title = request.POST.get('channel_title')
        video_date = request.POST.get('video_date')
        d1 = datetime.datetime.strptime(video_date,"%Y-%m-%dT%H:%M:%SZ")
        channel_profile = request.POST.get('channel_profile')
        video_thumbnail_pic = request.POST.get('video_thumbnail_pic')
        WatchListobj= WatchList.objects.create(user= request.user, video_title=video_title, video_description=video_description, video_id=video_id,channel_title=channel_title, upload_date=video_date,channel_profile_pic=channel_profile,video_thumbnail_pic= video_thumbnail_pic)
        WatchListobj.save()
        print('****************************** Ajax Req', video_description)
    # else:
    #     message = "Not Ajax"
    return HttpResponse('message')


def watch_list_view(request):
    all_videos= WatchList.objects.filter(user=request.user)
    context= {'all_videos': all_videos}
    return render(request, 'youtube/watch_list.html', context)

@csrf_exempt
def delete_watchlist_video(request):
    if request.method == 'POST':
        video_id= request.POST.get('video_id')
        video_obj= WatchList.objects.get(user= request.user, video_id= video_id)
        video_obj.delete()
    return HttpResponse('message')  


def channel_home_view(request):

    if request.method == 'POST':
        channel_id= request.POST.get('channel_id_home')
        print('*************** CHannel ID****************', channel_id)
        pl_request = youtube.playlists().list(
                part='snippet',
                channelId= channel_id,
        )
        video_request = youtube.search().list(
        part='snippet',
        type='video',
        channelId= channel_id,
        maxResults= 50
      ) 
        
        # To get the cahnnel profile pic
        request_channel_snippet = youtube.channels().list(
            part='snippet, statistics',
            id=channel_id 
        )
        watchlist_videos= WatchList.objects.filter(user=request.user)
        videos_id_list=[]
        for video in watchlist_videos:
            videos_id_list.append(video.video_id)
        response_channel_snippet=request_channel_snippet.execute()
        channel_snippet_items= response_channel_snippet['items']
        channel_snippet_item= channel_snippet_items[0]
        # End profile picture
        print('channel_snippet_item+++++++++++++++++++++',response_channel_snippet)
        response = pl_request.execute()
        video_reponse= video_request.execute()
        pl_items= response['items']
        video_items= video_reponse['items']
        context= {'pl_items': pl_items, 'video_items': video_items, 'channel_item': channel_snippet_item, 'watchlist_videos': videos_id_list}
        print('Playlist ___', video_reponse)
        return render(request, 'youtube/channel_home.html', context)


def search_view(request):
    
    try:
        if request.method== 'POST':
            search_keyword= request.POST.get('search_keyword')
            keyword_obj= Keyword.objects.filter(keyword__icontains=search_keyword)
            if (keyword_obj.exists()):
                keyword= keyword_obj[0]
                keyword_var= keyword.keyword
                catgegory_var=keyword.category.category
                search_var= keyword_var+','+catgegory_var
                video_request = youtube.search().list(
                        part='snippet',
                        type='video',
                        # q='Athletes,Football, Volleyball',
                        q=search_var,
                        maxResults=50,
                        order= 'date' 
                    )
                video_response = video_request.execute()
                video_items= video_response['items']
                country_list=["Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antigua & Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia & Herzegovina","Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Canada","Cape Verde","Cayman Islands","Central Arfrican Republic","Chad","Chile","China","Colombia","Congo","Cook Islands","Costa Rica","Cote D Ivoire","Croatia","Cuba","Curacao","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France","French Polynesia","French West Indies","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea Bissau","Guyana","Haiti","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kiribati","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Myanmar","Namibia","Nauro","Nepal","Netherlands","Netherlands Antilles","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","North Korea","Norway","Oman","Pakistan","Palau","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico","Qatar","Reunion","Romania","Russia","Rwanda","Saint Pierre & Miquelon","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Korea","South Sudan","Spain","Sri Lanka","St Kitts & Nevis","St Lucia","St Vincent","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor L'Este","Togo","Tonga","Trinidad & Tobago","Tunisia","Turkey","Turkmenistan","Turks & Caicos","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States of America","Uruguay","Uzbekistan","Vanuatu","Vatican City","Venezuela","Vietnam","Virgin Islands (US)","Yemen","Zambia","Zimbabwe"];
                json_list= json.dumps(country_list)
                watchlist_videos= WatchList.objects.filter(user=request.user)
                All_keywords= Keyword.objects.all()
                videos_id_list=[]
                for video in watchlist_videos:
                    videos_id_list.append(video.video_id)
                context= {'data': video_items, 'watchlist_videos': videos_id_list, 'all_keywords': All_keywords, 'country_list': country_list}
                return render(request, 'youtube/search.html', context)
            else:
                message= 'Sorry! No Search Result Found'
                context= {'message': message}
                return render(request, 'youtube/search.html', context)
    except:
        message= 'Sorry! No Search Result Found'
        context= {'data': "",'message': message}
        return render(request, 'youtube/search.html', context)
def auto_complete(request):
    
    All_keywords= Keyword.objects.all()
    keywords_list=[]
    for keyword in All_keywords:
        keywords_list.append(keyword.keyword)
    print(keywords_list)   
    return JsonResponse({'data': keywords_list,})
    # return HttpResponse(json_list)






# Update data of the site in the database every 24 hour 

def update_data_db(request):
    all_keywords= Keyword.objects.all()
    keyword_var=''
    data_list= []
    dummy_data_list=[]
    for keyword in all_keywords:
        keyword_var= keyword.keyword
        catgegory_var=keyword.category.category
        search_var= keyword_var+','+catgegory_var
        print('*************search_var', search_var)     
        video_request = youtube.search().list(
            part='snippet',
            type='video',
            # q='Athletes,Football, Volleyball',
            q=search_var,
            maxResults=15,
            order= 'date'
            
        
        )
        list=[]
        video_response = video_request.execute()
        video_items= video_response['items']
        data_list = data_list+video_items
        all_data_obj= AllData.objects.get(id=1)
        all_data_obj.data=data_list
        all_data_obj.save()
        keyword.data=video_items
        keyword.save()
    return redirect('/watchlist')
        
@csrf_exempt
def filter_videos_home(request):
    if request.method == 'POST':
        filter_category= request.POST.get('filter_category')
        filter= request.POST.get('filter')
        print('category', filter_category)
        print('filter',filter)
        All_keywords= Keyword.objects.filter(category__category = filter_category)
        keywords_data_list= []
        videos_api_data=[]
        keywords_string=""
        for keyword in All_keywords:
            keywords_data_list= keywords_data_list + (keyword.data)
        video_id_list=[]
        for data in keywords_data_list:
            video_id=data['id']['videoId']

            # print('video id', video_id)
            # keywords_string=keywords_string+ ','+ str(video_id)
            # print(keywords_string)
            video_id_list.append(video_id)
        divided_chunk_list = list(divide_chunks(video_id_list, 50))
        for chunk in divided_chunk_list:
            keywords_string=''
            for val in chunk:
                keywords_string=keywords_string+ ','+ str(val)
                keywords_string=keywords_string.lstrip(',')
            request = youtube.videos().list(
                        part="statistics,snippet",
                        id=keywords_string,
                        maxResults=1
                        )
            response = request.execute()
            items= response['items']
            # print(items)
            videos_api_data= videos_api_data+items
        # keywords_string=keywords_string.lstrip(',')
        # print(type(keywords_string))
        # request = youtube.videos().list(
        # part="statistics,snippet",
        # id=keywords_string,
        # maxResults=1
        # )
        # response = request.execute()
        # items= response['items']
        # print('videos', videos_api_data)
        for item in videos_api_data:
            id=item['id']
            print('id',id)
            likes= item['statistics']['likeCount']
            print('likes', type(likes), likes)
        sorted_l=sorted(videos_api_data, key=lambda x: int(x['statistics']['commentCount']), reverse=True)
        print(sorted_l)   
    return HttpResponse('success')


def test(request):
    str_1=['w9HJw2eXyqE,MeMUO_D1-pg,YjJvlhF8d5c,6vjpHJMBcsI,wEI3zqxNKbw,n2lRTW2zwNc,uacpjGQLvuE,_92PIn1wj0k,HFnPL255muo,frhuuVWC0JY,FORzH8zSrtg']
    str_2=['w9HJw2eXyqE','MeMUO_D1-pg','YjJvlhF8d5c','6vjpHJMBcsI','wEI3zqxNKbw','n2lRTW2zwNc','uacpjGQLvuE','_92PIn1wj0k','HFnPL255muo','frhuuVWC0JY','FORzH8zSrtg']
    
    print((str_2))
    n = 12
    # x=[]
    x = list(divide_chunks(str_2, n))
    for chunk in x:
        s=''
        for val in chunk:
            s=s+ ','+ str(val)
            s=s.lstrip(',')
            print(str(val))
        print('****************',s)
    # request = youtube.videos().list(
    #     part="statistics,snippet",
    #     id=str,
    #     maxResults=1
    # )
    # response = request.execute()
    # items= response['items']
    # for item in items:
    #     likes= item['statistics']['likeCount']
    #     print('likes', likes)
    # sorted_l=sorted(items, key=lambda x: x['statistics']['likeCount'])

    print(x)

    return HttpResponse(x)

# Yield successive n-sized
# chunks from l.
def divide_chunks(l, n):
     
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]