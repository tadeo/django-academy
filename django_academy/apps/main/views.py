# Create your views here.
from django.shortcuts import render_to_response
from django.template import loader, Context
from apps.main.models import MessagesSent

def home(request):
    return render_to_response('home.html')

def welcome(request):
    return render_to_response('welcome.html')

def contact(request):   
    if request.method == 'POST':
        name = request.POST.get('sender_name', '')
        email = request.POST.get('sender_email', '')
        message = request.POST.get('sender_message', '')
        sender_obj = MessagesSent(sender_name=name, sender_email=email, sender_message=message)
        sender_obj.save()
    return contactRetrive(request)   
    
def contactRetrive(request):
    messages = MessagesSent.objects.all()
    return render_to_response('messages_received.html', {'messages': messages})    