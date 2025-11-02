from django.urls import path
from .views import home, show_messages, show_posts, post_detail, create_post, update_post, delete_post, about_user
urlpatterns = [
    path('home',home,name='home'),
    path('all_messages',show_messages,name='all_messages'),
    path('all_posts',show_posts,name='all_posts'),
    path('detail_post/<int:post_pk>/',post_detail,name='detail_post'),
    path('post/new/',create_post,name='create_post'),
    path('update/<int:post_pk>/',update_post,name='update_post'),
    path('delete/<int:post_pk>/',delete_post,name='delete_post'),
    path('about_user',about_user,name='about_user'),
]