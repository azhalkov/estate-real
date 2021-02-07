from django.contrib import admin

# Register your models here.
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from subscribers.models import Subscriber


class SubscriberAdmin(ModelAdmin):
    """Модель подписчика"""
    model = Subscriber
    menu_label = 'Subscribers'
    menu_icon = 'placeholder'
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("email", "full_name",)
    search_fields = ("full_name", "email", )

modeladmin_register(SubscriberAdmin)