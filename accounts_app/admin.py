from django.contrib import admin
from .forms import UserCreationForm, UserChangeForm
from .models import User
from pages_app.admin import PostInline
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    inlines = [PostInline]
    list_display = ('username','last_login')

admin.site.register(User, UserAdmin)