from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('grocer', 'Grocer'),
        ('buyer', 'Buyer'),
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

class GrocerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.brand_name

class BuyerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    