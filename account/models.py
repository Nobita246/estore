from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import uuid
from base.emails import send_account_activation_email


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile", primary_key=True
    )
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True)
    profile_image = models.ImageField(
        upload_to="user_profile", null=True, blank=True)


def create_profile(sender, instance, **kwargs):
    try:
        email = instance.username
        email_token = str(uuid.uuid4())
        profile = Profile.objects.create(
            user=instance, email_token=email_token)
        send_account_activation_email(email, email_token)

    except Exception as e:
        print(e)


post_save.connect(create_profile, sender=User)
