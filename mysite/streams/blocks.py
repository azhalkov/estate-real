"""streams/blocks"""
from wagtail.core import blocks


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


class RichtextBlock(blocks.RichTextBlock):
    """Класс streams/blocks/RichtextBlock шаблон html в корневом templates/stream"""


    class Meta:
        template = "stream/richtext_block.html"
        icon = 'doc-fuul'
        label = 'Все поля'


class SimpleRichtextBlock(blocks.RichTextBlock):
    """Класс streams/blocks/RichtextBlock шаблон html в корневом templates/stream"""

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
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