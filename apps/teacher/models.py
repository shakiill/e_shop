from django.db import models

from apps.user.models import Teacher


# Create your models here.
class TeacherProfile(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='teacher_profile')
    joining_date = models.DateField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.teacher.name)
