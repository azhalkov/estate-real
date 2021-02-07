from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class SocialMediaSettings(BaseSetting):
    """Установки для соцсетей"""
    facebook = models.URLField(blank=True, null=True, help_text='Facebook Url')
    youtube = models.URLField(blank=True, null=True, help_text='Youtube Url')

    panels = [
        MultiFieldPanel([
            FieldPanel('facebook'),
            FieldPanel('youtube'),
        ], heading="Опции баннера"),
    ]
    # content_panels = Page.content_panels + [
    # ]


