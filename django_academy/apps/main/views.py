# Create your views here.
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home.html')

def subscribe(request):

    from django.core.context_processors import csrf
    context = {}
    context.update(csrf(request))
    if request.method == 'GET':
        context.update({'message':{
                                       'type': 'initial',
                                       'text': 'Please put your name.'
                                       }
                        })
    elif request.method == 'POST':
        user_name = request.POST['name']
        if user_name == '':
            context.update({'message':{
                                       'type': 'error',
                                       'text': 'Please put a name.'
                                       }
                            })
        elif len(user_name)<3:
            context.update({'message':{
                                       'type': 'error',
                                       'text': 'Please put a name longer than 2 characters.'
                                       }
                            })
        else:
            context.update({'message':{
                                       'type': 'success',
                                       'text': 'Thank you %s.' % user_name
                                       }
                            })
        if context['message']['type'] == 'error':
            context.update({'posted_data': request.POST})

        print '>>>>>>> %s' % user_name

    return render_to_response('subscribe.html', context)