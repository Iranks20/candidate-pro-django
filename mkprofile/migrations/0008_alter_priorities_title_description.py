# Generated by Django 4.2.2 on 2023-10-16 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkprofile', '0007_prioritiesexamples_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priorities',
            name='title_description',
            field=models.TextField(null=True),
        ),
    ]
