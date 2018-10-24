from django.contrib import admin
from django.urls import path

from tweets import views
app_name="tweets"

urlpatterns = [
    
    path('',views.index, name="index_view"),
    path('list_tweet/',views.ListTweets.as_view(),name="list_view"),
    path('detail_tweet/<int:pk>',views.DetailTweet.as_view(),name="detail_view"),
    path('create/',views.Create.as_view(), name="create_view"),
    path('update/<int:pk>',views.UpdateTweet.as_view(),name="update_view"),
    path('delete/<int:pk>',views.DeleteTweet.as_view(), name="delete_view"),
]