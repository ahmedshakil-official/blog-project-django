from django.urls import path
from . import views

app_name = 'App_Blog'
urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('write/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/<slug:slug>/', views.blog_details, name='blog_details'),
    path('likeed/<pk>/', views.liked, name='liked_post'),
    path('unlikeed/<pk>/', views.unliked, name='unliked_post'),
    path('my-blog/', views.MyBlog.as_view(), name='my_blog'),
    path('update-blog/<pk>', views.UpdateBlog.as_view(), name='update_blog'),
    path('delete-blog/<pk>', views.DeleteBlog.as_view(), name='delete_blog'),

]