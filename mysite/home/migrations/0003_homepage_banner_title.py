# Generated by Django 3.1.6 on 2021-02-02 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]