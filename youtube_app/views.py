from multiprocessing import context
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

    youtube = build('youtube', 'v3', developerKey=api_key_2)

    request1 = youtube.channels().list(
            part='contentDetails',
            forUsername='schafer5'
        )
    request_channel_snippet = youtube.channels().list(
            part='snippet',
            forUsername='schafer5' 
        )

    response = request1.execute()
    response_channel_snippet=request_channel_snippet.execute()
    print('response****************',response)
    items=response['items']
    snippet_items= response_channel_snippet['items']
    snippet_item= snippet_items[0]
    profile_picture= snippet_item['snippet']['thumbnails']['default']['url']

    item=items[0]
    content= item['contentDetails']
    playlist= content['relatedPlaylists']
    uploads=playlist['uploads']
    # print(response)
    # print(uploads)

    video_request = youtube.search().list(
        part='snippet',
        type='video',
        q=' footlball,athletics',
        maxResults= 50
      )
    list=[]
    video_response = video_request.execute()
    video_items= video_response['items']
   
    watchlist_videos= WatchList.objects.filter(user=request.user)
    videos_id_list=[]
    for video in watchlist_videos:
        videos_id_list.append(video.video_id)
    print(videos_id_list)
    context= {'data': video_items, 'watchlist_videos': videos_id_list}
    return render(request, 'youtube/home.html', context)


def video_view(request):
    
    youtube = build('youtube', 'v3', developerKey=api_key_2)
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
    youtube = build('youtube', 'v3', developerKey=api_key_2)
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
        
        
        response = pl_request.execute()
        video_reponse= video_request.execute()
        pl_items= response['items']
        video_items= video_reponse['items']
        context= {'pl_items': pl_items, 'video_items': video_items}
        print('Playlist ___', video_reponse)
        return render(request, 'youtube/channel_home.html', context)
