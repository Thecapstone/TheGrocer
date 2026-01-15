from django.contrib import admin
from .models import CustomUser, GrocerProfile, BuyerProfile

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(GrocerProfile)
admin.site.register(BuyerProfile)