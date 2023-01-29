import time
from django.core.mail import EmailMessage
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string

from apps.user.models import CustomUser, Otp


#
#
# @receiver(post_save, sender=Otp)
# def otp_mail(sender, instance, created, *args, **kwargs):
#     if created:
#         ctx = {
#             'otp': instance.otp,
#         }
#         subject = "Registration OTP"
#         to = [instance.user, ]
#         # to.append(instance.jobseeker.email)
#         from_email = 'demo@demo.com'
#         message = render_to_string('otp.html', ctx)
#         msg = EmailMessage(subject, message, to=to, from_email=from_email)
#         msg.content_subtype = 'html'
#         msg.send()
