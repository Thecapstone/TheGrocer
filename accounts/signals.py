from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, GrocerProfile, BuyerProfile

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'grocer':
            GrocerProfile.objects.create(user=instance)
        else:
            BuyerProfile.objects.create(user=instance)