"""flex/models.py    https://www.youtube.com/watch?v=2f0Yjx84PAQ&list=PLMQHMcNi6ocsS8Bfnuy_IDgJ4bHRRrvub&index=7 """
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page


class FlexPage(Page):
    """Класс приложения Flex, страница"""
    template = 'flex/flex_page.html'

    subtitle = models.CharField('Суперзаголовок', max_length=100, blank=True, null=True)
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
    ]

    class Meta:
        verbose_name = 'Страница Flex'
        verbose_name_plural = 'Страницы '



