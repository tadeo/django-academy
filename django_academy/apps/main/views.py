# Create your views here.
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home.html')

def subscribe(request):
    return render_to_response('subscribe.html')