# Generated by Django 4.1.5 on 2023-02-02 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("store", "0002_alter_product_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="artist",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.CreateModel(
            name="ReviewRating",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(blank=True, max_length=500)),
                ("review", models.TextField(blank=True, max_length=100)),
                ("rating", models.FloatField()),
                ("ip", models.CharField(blank=True, max_length=20)),
                ("status", models.BooleanField(default=True)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]