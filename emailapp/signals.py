from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Our Website'
        message = f'Hi {instance.first_name},\n\nThank you for registering at our site.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]
        send_mail(subject, message, email_from, recipient_list)
