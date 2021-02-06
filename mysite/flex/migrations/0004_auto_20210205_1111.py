# Generated by Django 3.1.6 on 2021-02-05 11:11

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0003_auto_20210205_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Пишите заголовок', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Добавьте текст', required=True))])), ('fuul_richtext', streams.blocks.RichtextBlock()), ('simple_richtext', streams.blocks.SimpleRichtextBlock())], blank=True, null=True),
        ),
    ]
