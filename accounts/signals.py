from django_rest_passwordreset.signals import reset_password_token_created
from django.urls import reverse
from django.core.mail import send_mail
from django.dispatch import receiver
from .mail import mail_send


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Here reset-password-token-created have a signal through which password is receiving here in models file.
    """
    url = instance.request.build_absolute_uri(reverse('password-reset-confirm'))
    email_plaintext_message = "{}?token={}".format(url,
                                                   reset_password_token.key)
    """
    here it creates a plain text area where token of reset_password is available. From here this token passed
    to send_mail method.
    """
    mail_send(email_plaintext_message, reset_password_token)
