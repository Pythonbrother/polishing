from django.shortcuts import render,HttpResponse
from .models import message
# Create your views here.
def home(request):
    return render(request, 'home.html')

def show_messages(request):
    all_messages = message.objects.all()
    return render(request, 'all_message.html', {'messages':all_messages})