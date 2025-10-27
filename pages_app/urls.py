from django.urls import path
from .views import home, show_messages, show_posts, post_detail
urlpatterns = [
    path('home',home,name='home'),
    path('all_messages',show_messages,name='all_messages'),
    path('all_posts',show_posts,name='all_posts'),
    path('detail_post/<int:post_pk>/',post_detail,name='detail_post')
]