# Create your views here.
from django.shortcuts import render_to_response
from apps.main.models import Subscriber, Course
from apps.main.forms import SubscribeForm
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail


def send_email(user_name, user_email, user_message):
    subject = 'New subscriber at Django Academy'
    message_body = '''%s <%s> posted the following message:
%s
    ''' % (user_name, user_email, user_message)
    first_user = User.objects.all()[0]
    recipients = [first_user.email]
    send_mail(subject, message_body, user_email, recipients, fail_silently=False)
#    try:
#    except Exception:
#        print 'error trying to send email'
#        pass


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

            user_name = form.cleaned_data['user_name']
            user_email = form.cleaned_data['email']
            user_message = form.cleaned_data['message']

            send_email(user_name, user_email, user_message)

            context.update({'message': 'Thank you %s' % user_name})
            new_subscriber = Subscriber(name=user_name, email=user_email)
            new_subscriber.save()
        else:
            context.update({'form': form})

    list_subscribers = Subscriber.objects.all().order_by('-id')
    context.update({'list_subscribers': list_subscribers})
    return render_to_response('subscribe.html', context)


def list_courses(request):
    from django.core.context_processors import csrf
    context = {}
    context.update(csrf(request))
    
    list_courses = Course.objects.all().order_by('name')
    context.update({'list_courses':list_courses})
    return render_to_response('list_courses.html', context)
    
class SubscriberDetailView(DetailView):
    def get(self, *args, **kwargs):
        return super(SubscriberDetailView, self).get(*args, **kwargs)

class CourseDetailView(DetailView):
    def get(self, *args, **kwargs):
        return super(CourseDetailView, self).get(*args, **kwargs)

