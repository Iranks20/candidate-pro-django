# Generated by Django 4.2.6 on 2023-11-11 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkprofile', '0027_remove_checkoutorder_postcode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutorder',
            name='delivery_cost',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='checkoutorder',
            name='total_cost',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='checkoutorder',
            name='unit_cost',
            field=models.TextField(null=True),
        ),
    ]
