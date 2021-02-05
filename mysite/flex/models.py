"""flex/models.py    https://www.youtube.com/watch?v=2f0Yjx84PAQ&list=PLMQHMcNi6ocsS8Bfnuy_IDgJ4bHRRrvub&index=7 """
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from streams import blocks


class FlexPage(Page):
    """Класс приложения Flex, страница"""
    template = 'flex/flex_page.html'
    subtitle = models.CharField('Суперзаголовок', max_length=100, blank=True, null=True)
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ('fuul_richtext', blocks.RichtextBlock()),
            ('simple_richtext', blocks.SimpleRichtextBlock()),
        ],
    null=True,
    blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        StreamFieldPanel("content"),
    ]

    class Meta:
        verbose_name = 'Страница Flex'
        verbose_name_plural = 'Страницы '



