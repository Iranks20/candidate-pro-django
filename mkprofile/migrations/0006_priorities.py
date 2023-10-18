# Generated by Django 4.2.2 on 2023-10-16 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkprofile', '0005_alter_campaign_background_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priorities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_description', models.CharField(max_length=100, null=True)),
                ('news_heading', models.TextField()),
                ('news_description', models.TextField()),
                ('news_image', models.ImageField(null=True, upload_to='news_images/')),
            ],
        ),
    ]
