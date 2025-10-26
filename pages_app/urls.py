from django.urls import path
from .views import home, show_messages
urlpatterns = [
    path('home',home,name='home'),
    path('all_messages',show_messages,name='all_messages'),
]