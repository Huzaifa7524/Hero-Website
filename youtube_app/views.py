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


# Youtube API Key
api_key= 'AIzaSyAzaAIFiU2QKcD4sqC47j-I9-0fAk3awHw'
api_key_2='AIzaSyAo9njxj8OJpWshmpCyamYf9GJXN-kIi64'
api_key_3='AIzaSyBztkmRfxkYWS9QCtS9XD8r6clecRBVK2s'
api_key_4='AIzaSyA4Mt5QJqtcTJ77BHIeFAj12M6s5mSUiFQ'
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

    # api_key = '#YOURAPIKEY'

    youtube = build('youtube', 'v3', developerKey=api_key_4)

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
    all_keywords= Keyword.objects.all()
    keyword_var=''
    data_list= []
    dummy_data_list=[]
    for keyword in all_keywords:
        keyword_var= keyword.keyword
     
        video_request = youtube.search().list(
            part='snippet',
            type='video',
            # q='Athletes,Football, Volleyball',
            q=keyword_var,
            maxResults=15,
            order= 'date'
            
        
        )
        list=[]
        video_response = video_request.execute()
        video_items= video_response['items']
        
       
        
        data_list= data_list+video_items
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
    
    youtube = build('youtube', 'v3', developerKey=api_key_4)
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
    youtube = build('youtube', 'v3', developerKey=api_key_4)
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



def test(request):
    return render(request, 'youtube/home_2.html')
