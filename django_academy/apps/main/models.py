from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subscriber(models.Model):

    class Meta:
        verbose_name = _('Subscriber')
        verbose_name_plural = _('Subscribers')

    name = models.CharField(max_length=400, blank=True, null=True, verbose_name=_('name'))

    def __unicode__(self):
        return u'Subscriber %s' % self.name
