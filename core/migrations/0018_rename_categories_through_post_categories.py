# Generated by Django 5.0.6 on 2025-03-27 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0017_remove_post_categories"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="categories_through",
            new_name="categories",
        ),
    ]
