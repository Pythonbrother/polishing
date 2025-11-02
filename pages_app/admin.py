from django.contrib import admin
from .models import message, Post
# Register your models here.

class PostInline(admin.TabularInline):
    model = Post
    extra = 1

admin.site.register(message)
admin.site.register(Post)