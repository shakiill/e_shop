from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Group
from django.db import models


class StaffManager(BaseUserManager):
    def get_queryset(self):
        return super(StaffManager, self).get_queryset().filter(is_staff=True, is_superuser=False)


class TeacherManager(BaseUserManager):
    def get_queryset(self):
        return super(TeacherManager, self).get_queryset().filter(groups__name='teacher')


class ParentManager(BaseUserManager):
    def get_queryset(self):
        return super(ParentManager, self).get_queryset().filter(groups__name='parent')


class StudentManager(BaseUserManager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(groups__name='student')
