from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

from streams import blocks


class BlogAvtor(models.Model):
    """Сниппет автора блога"""
    name = models.CharField('Ф.И.О.', max_length=100, default='Имя и фамилия')
    website = models.URLField('Ссылка на сайт', blank=True, null=True)
    avatar = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name = '+'
    )
    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                ImageChooserPanel("avatar"),
            ],
            heading="Имя и фото"
        ),
        MultiFieldPanel(
            [
                FieldPanel("website"),
            ],
            heading='Ссылка'
        )
    ]
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор блога'
        verbose_name_plural = 'Авторы'

register_snippet(BlogAvtor)



class BlogListingPage(Page):
    """Listing page lists all the Blog Detail Pages."""

    template = "blog/blog_listing_page.html"

    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = BlogDetailPage.objects.live().public()
        context['authors'] = BlogAvtor.objects.all()
        return context

    def get_sitemap_urls(self, request=None):
        sitemap = super().get_sitemap_urls(request)
        sitemap.append(
            {
                "location": self.full_url,
                "lastmod": self.latest_revision_created_at,
                'changefreq': 'monthly',
                'priority': 1
            }
        )

        return sitemap



class BlogDetailPage(Page):
    """Blog detail page."""
    template = 'blog/blog_detail_page.html'

    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )
    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
            ("simple_richtext", blocks.SimpleRichtextBlock()),
            ("cards", blocks.CardBlock()),
            ("cta", blocks.CTABlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        ImageChooserPanel("blog_image"),
        StreamFieldPanel("content"),
    ]



class BlogPage(Page):

    # Database fields
    zagolovok = models.CharField('Заголовок', max_length=70, blank=True, null=True)
    body = RichTextField()
    date = models.DateField("Post date")
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    content = StreamField(
        [
            ('fuul_richtext', blocks.RichtextBlock()),
        ],
        null=True,
        blank=True,
    )
    """Поля в админке """
    content_panels = Page.content_panels + [
        FieldPanel('zagolovok'),
        FieldPanel('date'),
        FieldPanel('body', classname="full"),
        InlinePanel('related_links', label="Related links"),
        StreamFieldPanel("content"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        ImageChooserPanel('feed_image'),
    ]


    # Parent page / subpage type rules

    # parent_page_types = ['blog.BlogIndex']
    subpage_types = []


class BlogPageRelatedLink(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='related_links')
    name = models.CharField(max_length=255)
    url = models.URLField()

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
    ]



