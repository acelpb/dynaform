from django.contrib import admin

# Register your models here.
from .models import Message


@admin.register(Message)
class PreferenceAdmin(admin.ModelAdmin):
    pass
