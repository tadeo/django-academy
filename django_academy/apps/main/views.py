# Create your views here.
from django.shortcuts import render_to_response
from apps.main.forms import SubscribeForm

def home(request):
    return render_to_response('home.html')

def subscribe(request):
    from django.core.context_processors import csrf
    context = {}
    context.update(csrf(request))
    empty_form = SubscribeForm()
    if request.method == 'GET':
        context.update({'form': empty_form})
    elif request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            context.update({'form': empty_form})
            context.update({'message': 'Thank you %s' % form.cleaned_data['user_name']})
            print '>>>>>>> %s' % form.cleaned_data['user_name']
        else:
            context.update({'form': form})

#        print '>>>>>>> %s' % user_name

    return render_to_response('subscribe.html', context)