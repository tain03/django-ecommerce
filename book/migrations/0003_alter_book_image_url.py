# Generated by Django 5.1.5 on 2025-02-19 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_book_image_book_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image_url',
            field=models.URLField(blank=True, max_length=10000, null=True),
        ),
    ]
