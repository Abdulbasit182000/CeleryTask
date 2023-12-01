from django.contrib import admin

from .models import CustomUser, Person

# Register your models here.
admin.site.register(Person)
admin.site.register(CustomUser)
