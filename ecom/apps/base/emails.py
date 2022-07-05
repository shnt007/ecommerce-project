from django.conf import settings
from django.core.mail import send_mail


def send_account_activation_email(email, email_token):
    subject = 'Your account needs to be verified'
    from_email = settings.EMAIL_HOST_USER
    message = f'Hi, Click on the link to activate your account http://127.0.0.1:8000/accounts/activate/{email_token}.'
    send_mail(subject, message, from_email, [email])
