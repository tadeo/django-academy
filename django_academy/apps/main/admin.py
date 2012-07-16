from django.contrib import admin
from apps.main.models import Subscriber, Student, Course, UserProfile

admin.site.register(Subscriber)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(UserProfile)