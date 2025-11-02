from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .models import message, Post
from .forms import PostCreateForm, PostUpdateForm
from django.contrib.auth import get_user_model
from django.contrib import messages
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

def create_post(request):
    if request.method == 'GET':
        form = PostCreateForm()
        return render(request, 'create_post.html', {'form':form})
    else:
        form = PostCreateForm(request.POST)
        User = get_user_model()
        if form.is_valid():
            title = form.cleaned_data['title']
            topic = form.cleaned_data['topic']
            author = User.objects.first()
            post = Post(title=title,topic=topic,author=author)
            post.save()
            current_post = post
            return redirect('detail_post', current_post.id)

def update_post(request, post_pk):
    post = get_object_or_404(Post, id=post_pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            topic = form.cleaned_data['topic']
            post.title = title
            post.topic = topic
            post.save()
            return redirect('detail_post', post.id)
    else:
        form = PostUpdateForm(initial={'title':post.title,'topic':post.topic})
    return render(request, 'update_post.html', {'form':form})

def delete_post(request, post_pk):
    post = get_object_or_404(Post, id=post_pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    else:
        return render(request, 'delete_post.html', {'post':post})

def about_user(request):
    return render(request, 'about_user.html')