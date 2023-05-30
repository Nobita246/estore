from django.conf import settings
from django.core.mail import send_mail


def send_account_activation_email(email, email_token):
    subject = "Youe account need to verify."
    email_from = settings.EMAIL_HOST_USER
    message = (
        "Hi, Click this following link to verify your account "
        + settings.APP_BASE_URL
        + "account/activate/user/"
        + email_token
    )

    send_mail(subject, message, email_from, [email])
    return True
