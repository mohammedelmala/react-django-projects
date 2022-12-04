from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile


@receiver(post_save, sender=User)
def post_save_user_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile.objects.create(user=instance)
        print(f'Profile created successfully for user {instance}')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            profile = UserProfile.objects.create(user=instance)
            print(f"Profile for {instance} was not exist but we created one")


@receiver(pre_save, sender=User)
def pre_save_user_createprofile_receiver(sender, instance, **kwargs):
    pass



