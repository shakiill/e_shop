import datetime

from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from apps.user.managers import StaffManager, ParentManager, TeacherManager, StudentManager
from e_shop import settings


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
    is_verified = models.BooleanField(default=False)
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


class Otp(models.Model):
    user = models.CharField(max_length=15, editable=False)
    otp = models.CharField(max_length=40, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    attempts = models.IntegerField(default=0)
    used = models.BooleanField(default=False)

    class Meta:
        verbose_name = "OTP Token"
        verbose_name_plural = "OTP Tokens"

    def __str__(self):
        return "{} - {}".format(self.user, self.otp)

    # @classmethod
    # def create_otp_for_number(cls, number):
    #     today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    #     today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    #     otps = cls.objects.filter(phone_number=number, timestamp__range=(today_min, today_max))
    #
    #     if otps.count() <= getattr(settings, 'PHONE_LOGIN_ATTEMPTS', 100000):
    #         otp = cls.generate_otp(length=getattr(settings, 'PHONE_LOGIN_OTP_LENGTH', 4))
    #         phone_token = PhoneToken(phone_number=number, otp=otp)
    #         phone_token.save()
    #         # if settings.DEBUG:
    #         #     print(f'Your otp is {otp}')
    #         # else:
    #         #     send_sms(number, f'Your otp is {otp}')
    #         return phone_token
    #     else:
    #         return False
    #
    # @classmethod
    # def generate_otp(cls, length=4):
    #     hash_algorithm = getattr(settings, 'PHONE_LOGIN_OTP_HASH_ALGORITHM', 'sha256')
    #     m = getattr(hashlib, hash_algorithm)()
    #     m.update(getattr(settings, 'SECRET_KEY', None).encode('utf-8'))
    #     m.update(os.urandom(16))
    #     # otp = str(int(m.hexdigest(), 16))[-length:]
    #     otp = 1234
    #     return otp


@receiver(post_save, sender=CustomUser)
def otp_create(sender, instance, created, *args, **kwargs):
    if created:
        Otp.objects.create(
            user=instance.username,
            otp=get_random_string(length=6, allowed_chars='0123456789')
        )
