from django.db import models
from django.contrib import admin

class MessagesSent(models.Model):
    sender_name = models.CharField(max_length=80)
    sender_email = models.EmailField()
    sender_message = models.TextField()

admin.site.register(MessagesSent)