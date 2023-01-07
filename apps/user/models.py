from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils.crypto import get_random_string

from apps.user.managers import StaffManager, ParentManager, TeacherManager, StudentManager


# Create your models here.


class CustomUser(AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'Male',
        FEMALE = 'Female',
        OTHER = 'Other',

    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    last_name = None
    first_name = None
    phone_number = models.CharField(max_length=15, null=True, blank=True, unique=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=Gender.choices, default=Gender.MALE, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(verbose_name='Email Address', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    updated_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')

    def __str__(self):
        return str(self.username)


class Staff(CustomUser):
    class Meta:
        proxy = True

    objects = StaffManager()

    def save(self, *args, **kwargs):
        self.is_staff = True
        # password = get_random_string(length=6, allowed_chars='ABCD0123456789')
        password = 'demo@1234'
        self.set_password(password)
        super(Staff, self).save(*args, **kwargs)
        # send sms script


class Parent(CustomUser):
    class Meta:
        proxy = True

    objects = ParentManager()

    def save(self, *args, **kwargs):
        super(Parent, self).save(*args, **kwargs)
        group, created = Group.objects.get_or_create(name='parent')
        self.groups.set([group])


class Student(CustomUser):
    class Meta:
        proxy = True

    objects = StudentManager()

    def save(self, *args, **kwargs):
        super(Student, self).save(*args, **kwargs)
        group, created = Group.objects.get_or_create(name='student')
        self.groups.set([group])


class Teacher(CustomUser):
    class Meta:
        proxy = True

    objects = TeacherManager()

    def save(self, *args, **kwargs):
        super(Teacher, self).save(*args, **kwargs)
        group, created = Group.objects.get_or_create(name='teacher')
        self.groups.set([group])
