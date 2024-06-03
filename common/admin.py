from django.contrib import admin
from .models import *


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'file_type']
    list_filter = ['id']
    search_fields = ['file_type']


@admin.register(CommonSettings)
class CommonSettingsAdmin(admin.ModelAdmin):
    list_display = ['main_phone_number', 'main_email_address', 'main_text', 'main_delivery_text',
                    'main_banner_image', 'main_bottom_image']


