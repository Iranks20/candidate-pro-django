# Generated by Django 4.2.6 on 2023-11-07 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkprofile', '0023_event_end_time_event_location_event_start_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='customer_review',
            field=models.TextField(blank=True, null=True),
        ),
    ]
