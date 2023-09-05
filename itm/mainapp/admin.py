from django.contrib import admin
from authapp.models import CustomUser


@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    pass
