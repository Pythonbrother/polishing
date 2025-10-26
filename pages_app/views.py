from django.shortcuts import render,HttpResponse
# Create your views here.
def greeting(request):
    return render(request, 'greeting.html')