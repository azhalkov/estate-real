# home/models
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel


class HomePage(Page):
    """ Главная страница модель home, создаем
    поля для сохранения в базе данных (наследуем от wagtail и django)"""
    templates = 'home/home_page.html'
    max_count = 1
    banner_title = models.CharField(max_length=100, blank=True, null=True, help_text='Для пля Title')
    banner_subtitle = RichTextField(features=['bold', 'italic', 'h3', 'h4' ], blank=True, null=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Для загрузки изображений',
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    book_file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='Для загрузки документов',
        related_name='+'
    )

    """Поля для админки (content_panels)"""
    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
        PageChooserPanel("banner_cta"),
        DocumentChooserPanel('book_file'),
    ]

    # panels = pass

    class Meta:
        verbose_name = "shablon_Home"
        verbose_name_plural = "Verbose_name_plural"

