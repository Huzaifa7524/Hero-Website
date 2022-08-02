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

    path('auto_complete/', views.auto_complete, name='auto_complete'),

    # Update data in db
    path('update_data_db/', views.update_data_db, name='update_data_db'),

    # Update data in home page AJAX
    path('update_data_home_ajax/', views.home_data_ajax, name='update_data_home_ajax'),

    # for testing purposes
    path('test/', views.test, name='test'),
    
   
]
