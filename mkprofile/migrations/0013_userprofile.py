# Generated by Django 4.2.6 on 2023-10-18 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkprofile', '0012_products_alter_testimonials_testimonial_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('address', models.TextField(blank=True)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
                ('activities', models.CharField(blank=True, max_length=200)),
                ('comments', models.TextField(blank=True)),
            ],
        ),
    ]
