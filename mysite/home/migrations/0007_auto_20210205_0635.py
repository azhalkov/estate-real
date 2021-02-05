# Generated by Django 3.1.6 on 2021-02-05 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0010_document_file_hash'),
        ('wagtailimages', '0022_uploadedimage'),
        ('home', '0006_auto_20210204_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='banner_image',
            field=models.ForeignKey(blank=True, help_text='Для загрузки изображений', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='book_file',
            field=models.ForeignKey(blank=True, help_text='Для загрузки документов', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document'),
        ),
    ]