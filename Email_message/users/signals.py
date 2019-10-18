from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail


@receiver(post_save, sender=User)
def send_email(sender, instance, **kwargs):
    msg = instance.username + ' has been successfully registered'
    """
        send_mail fxn takes following parameters:
        subject, message, from, to
    """
    send_mail('User Registered', msg, 'bbang2358@gmail.com', [instance.email, 'naween321@gmail.com',
                                                              'pnabiniw@gmail.com'], fail_silently=True)

