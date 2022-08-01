from django.urls import path,  include
from . import views
urlpatterns = [
    path('', views.loginUser, name='login'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('video_player/', views.video_view, name='video_player'),
    path('addvideotowatchlist/', views.add_to_watchlist, name='addvideotowatchlist'),
    path('watchlist/', views.watch_list_view, name='watchlist'),
    path('deletewatchlist/', views.delete_watchlist_video, name='deletewatchlist'),
    path('channelhome/', views.channel_home_view, name='channelhome'),
    path('search/', views.search_view, name='search'),


    path('test/', views.test, name='test'),
    
   
]
