# Generated by Django 4.2.6 on 2023-10-24 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkprofile', '0016_news_iframe'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='soundcloud_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]