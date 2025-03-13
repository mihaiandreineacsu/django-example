# Generated by Django 5.0.6 on 2025-03-13 09:14

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_alter_category_color"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="color",
            field=colorfield.fields.ColorField(
                default="#FFFFFF",
                help_text="The unique color of category.",
                image_field=None,
                max_length=25,
                samples=None,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                help_text="The unique name of Post category.",
                max_length=80,
                unique=True,
            ),
        ),
        migrations.AddConstraint(
            model_name="category",
            constraint=models.UniqueConstraint(
                models.F("color"),
                name="unique_color",
                violation_error_message="This Color already exists.",
            ),
        ),
    ]
