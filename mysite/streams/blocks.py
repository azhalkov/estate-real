"""streams/blocks"""
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock



class TitleAndTextBlock(blocks.StructBlock):
    """Заголовок и текст больше нечего Для вставки на страницу mysite/templates/flex/flex_page.html
    {% for block in page.content %}    {% include_block block %} {% endfor %}
    Редактировать блок по адресу mysite/templates/stream/title_and_text_block.html
    {{self.title}} {{self.text}} """

    title = blocks.CharBlock(required=True, help_text='Пишите заголовок')
    text = blocks.TextBlock(required=True, help_text='Добавьте текст')
    # mapping  = blocks.G

    class Meta:
        template = "stream/title_and_text_block.html"
        icon = "edit"
        label = "Заголовок и текст"


class CardBlock(blocks.StructBlock):
    """Карта - Фото, заголовок, урл, кнопка"""
    title = blocks.CharBlock(required=True, help_text='Пишите заголовок')
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="")),
            ]
        )
    )

    class Meta:
        template = "stream/card_block_block.html"
        icon = 'placeholder'
        label = 'Karti'


class RichtextBlock(blocks.RichTextBlock):
    """Класс streams/blocks/RichtextBlock шаблон html в корневом templates/stream"""

    class Meta:
        template = "stream/richtext_block.html"
        icon = 'doc-fuul'
        label = 'Все поля'


class SimpleRichtextBlock(blocks.RichTextBlock):
    """Класс streams/blocks/RichtextBlock шаблон html в корневом templates/stream"""

    def __init__(self,  **kwargs):  # required=True, help_text=None, editor='default', features=None, validators=(),
        super().__init__(**kwargs)
        self.features = [
            'bold',
            'italic',
            'link',
        ]

    class Meta:
        template = "stream/simple_richtext_block.html"
        icon = 'edit'
        label = 'Simpl richtext'


class CTABlock(blocks.StructBlock):
    """Простой звонок в раздел активации"""
    """https://www.youtube.com/watch?v=B1WXVIfiKXs&list=PLMQHMcNi6ocsS8Bfnuy_IDgJ4bHRRrvub&index=11"""
    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=['bold', 'italic'])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False, help_text='url')
    button_text = blocks.CharBlock(required=True, max_length=200, default='Нажать')

    class Meta:
        template = 'stream/cta_block.html'
        icon = 'placeholder'
        label = "Caal to Action"


class LinkStructValue(blocks.StructValue):
    """Логика для url"""

    def url(self):
        button_page = self.get('button_page')
        button_url = self.get('button_url')
        if button_page:
            return button_page
        elif button_url:
            return button_url

        return None


class ButtonBlock(blocks.StructBlock):
    """Внешний или внутренний URL"""

    button_page = blocks.PageChooserBlock(required=False, help_text='Выбор в первую очередь')
    button_url = blocks.URLBlock(required=False, help_text='Выбор - вторая очередь')

    # def get_context(self, request, *args, **kwargs):
    #     context = super().get_context(request, *args, **kwargs)
    #     context['latest_post'] = BlogDetailPage.objects.live().public()[:2]
    #     return context

    class Meta:
        template = 'stream/button_block.html'
        icon = 'placeholder'
        label = "Одна кнопка"
        value_class = LinkStructValue

