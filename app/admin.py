from django.contrib import admin
from .models import Film, Category
from django.contrib.auth.models import User, Group
# Register your models here.

admin.site.unregister(User)
admin.site.unregister(Group)


admin.site.register(Film)
admin.site.register(Category)

