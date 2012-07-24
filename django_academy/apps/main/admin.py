from django.contrib import admin
from apps.main.models import Subscriber, Student, Course, UserProfile, Teacher

admin.site.register(Subscriber)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(UserProfile)
admin.site.register(Teacher)
