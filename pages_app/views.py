from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import message, Post
# Create your views here.
def home(request):
    return render(request, 'home.html')

def show_messages(request):
    all_messages = message.objects.all()
    return render(request, 'all_message.html', {'messages':all_messages})

def show_posts(request):
    all_posts = Post.objects.all()
    return render(request, 'all_posts.html', {'posts':all_posts})

def post_detail(request,post_pk):
    post = get_object_or_404(Post, id=post_pk)
    return render(request, 'detail_post.html', {'post':post})