"""streams/blocks"""
from wagtail.core import blocks


class TitleAndTextBlock(blocks.StructBlock):
    """Заголовок и текст больше нечего"""

    title = blocks.CharBlock(required=True, help_text='Пишите заголовок')
    text = blocks.TextBlock(required=True, help_text='Добавьте текст')
    # mapping  = blocks.G

    class Meta:
        template = "stream/title_and_text_block.html"
        icon = "edit"
        label = "Заголовок и текст"



