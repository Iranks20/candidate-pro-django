# Generated by Django 4.2.2 on 2023-10-15 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkprofile', '0004_alter_campaign_background_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='background_image',
            field=models.ImageField(null=True, upload_to='campaign_backgrounds/'),
        ),
    ]