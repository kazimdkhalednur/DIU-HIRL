# Generated by Django 4.1.4 on 2024-08-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0040_research_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Dataset",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("description", models.TextField(max_length=1000)),
                ("image", models.FileField(upload_to="dataset/%y")),
                ("dataset_link", models.URLField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="Github",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("description", models.TextField(max_length=1000)),
                ("image", models.FileField(upload_to="github/%y")),
                ("github_link", models.URLField(blank=True, max_length=300)),
            ],
        ),
    ]
