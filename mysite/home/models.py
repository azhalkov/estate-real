# home/models
from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel

from streams import blocks

class HomePageCarouselImages(Orderable):
    """ 5 фото карусели домашней страницы"""
    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Для загрузки изображений',
    )

    panels = [
        ImageChooserPanel("carousel_image"),
    ]



class HomePage(Page):
    """ Главная страница модель home, создаем
    поля для сохранения в базе данных (наследуем от wagtail и django)"""
    show_in_menus_default = True
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

    content = StreamField(
        [
            ("cta", blocks.CTABlock()),
        ],
        blank = True,
        null=True,
    )

    """Поля для админки (content_panels)"""
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('banner_title'),
            FieldPanel("banner_subtitle"),
            ImageChooserPanel("banner_image"),
            PageChooserPanel("banner_cta"),
            DocumentChooserPanel('book_file'),
        ], heading="Опции баннера"),

        MultiFieldPanel([
            InlinePanel("carousel_images"),
        ], heading='Карусель фото'),
        StreamFieldPanel('content'),
    ]



    # panels = pass

    class Meta:
        verbose_name = "shablon_Home"
        verbose_name_plural = "Verbose_name_plural"

