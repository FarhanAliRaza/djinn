# Generated by Django 5.0.2 on 2024-03-05 20:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0007_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="category",
            field=models.ManyToManyField(blank=True, to="core.category"),
        ),
    ]
