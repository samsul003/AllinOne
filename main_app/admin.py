from django.contrib import admin
from .models import Category, Item, CategoryByUser

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(CategoryByUser)