from django.contrib import admin
from .models import UserProfile, Item, Order

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Item)
admin.site.register(Order)
