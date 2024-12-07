from django.contrib import admin
from django.urls import path,include
from tweet import views

urlpatterns = [
    path('', views.tweet_list, name="tweet_list"),
    path('tweet_create/',views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/tweet_edit/',views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/tweet_delete/',views.tweet_delete, name='tweet_delete'),
    path('user_login/',views.user_login,name="user_login"),
    path('user_register/',views.user_register,name="user_register"),
    path('user_logout/',views.user_logout,name="user_logout"),
]