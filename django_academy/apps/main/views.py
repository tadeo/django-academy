# Create your views here.
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home.html')

def welcome(request):
    return render_to_response('welcome.html')

def contact(request):
    #user_name = request.GET['full-name']
    return render_to_response('contact.html')