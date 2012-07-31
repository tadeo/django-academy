from django.contrib import admin
from apps.main.models import Subscriber, Student, Course, UserProfile, Teacher



class StudentAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'user_profile', 'course', 'approved')
    search_fields = ['course__name', 'user_profile__user__last_name']
    list_filter = ('approved', 'course')
    list_per_page = 10
    list_editable = ('approved',)

class ApprovedStudentInline(admin.options.TabularInline):
    model    = Student
    extra    = 1
    def queryset(self, request):
        return Student.objects.filter(approved=True)

class NotApprovedStudentInline(admin.options.TabularInline):
    model    = Student
    extra    = 1
    def queryset(self, request):
        return Student.objects.filter(approved=False)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'name', 'start_date')
    list_editable = ('name', 'start_date')
    inlines = [ApprovedStudentInline, NotApprovedStudentInline]

admin.site.register(Subscriber)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(UserProfile)
admin.site.register(Teacher)
