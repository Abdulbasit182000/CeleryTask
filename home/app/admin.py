from django.contrib import admin

from .models import CustomUser


class Custom_User_List_Display(admin.ModelAdmin):
    list_display = ("email", "date_of_birth", "is_changed")


admin.site.register(CustomUser, Custom_User_List_Display)
