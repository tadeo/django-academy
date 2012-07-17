from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Subscriber(models.Model):

    class Meta:
        verbose_name = _('Subscriber')
        verbose_name_plural = _('Subscribers')

    name = models.CharField(max_length=400, verbose_name=_('name'))
    last_name = models.CharField(max_length=400, blank=True, null=True, verbose_name=_('last name'))
    email = models.EmailField(verbose_name=_('email'))

    def __unicode__(self):
        return u'Subscriber %s' % self.name


class Course(models.Model):
    ''' '''
    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')

    name = models.CharField(max_length=400, verbose_name=_('name'))
    description = models.TextField(blank=True, null=True, verbose_name=_('description'))
    active = models.BooleanField(default=False, verbose_name=_('active'))
    start_date = models.DateField(blank=True, null=True, verbose_name=_('start_date'))
    end_date = models.DateField(blank=True, null=True, verbose_name=_('end_date'))

    def __unicode__(self):
        return u'Course %s' % self.name


class UserProfile(models.Model):
    '''A model representing a Person'''
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.get_full_name() or self.user


class Student(models.Model):
    '''A model representing the Person-Course relationship (score, assistances, etc)'''

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    user_profile = models.ForeignKey(UserProfile)
    course = models.ForeignKey(Course)
    approved = models.BooleanField(default=False)

    def __unicode__(self):
        return u'Student %s at %s' % (self.user_profile, self.course)