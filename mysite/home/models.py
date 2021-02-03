from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.core.models import Page


class HomePage(Page):
    """ Главная страница модель home"""
    templates = 'home/myhome_page.html'
    banner_title = models.CharField(max_length=100, blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
    ]

