# Generated by Django 5.0.6 on 2025-03-27 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_postcategory"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="categories_through",
            field=models.ManyToManyField(
                through="core.PostCategory", to="core.category"
            ),
        ),
    ]
