# Generated by Django 4.2.6 on 2023-10-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkprofile', '0015_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='iframe',
            field=models.URLField(blank=True, null=True),
        ),
    ]
