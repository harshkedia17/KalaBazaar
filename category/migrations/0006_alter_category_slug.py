# Generated by Django 4.1.5 on 2023-01-31 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0005_alter_category_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(
                blank=True, editable=False, max_length=100, unique=True
            ),
        ),
    ]
