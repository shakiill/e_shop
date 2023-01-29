from django.contrib import admin

from apps.user.models import CustomUser, Staff, Teacher, Parent, Student, Otp

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Staff)
admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(Otp)
