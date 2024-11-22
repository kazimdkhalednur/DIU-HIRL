# Generated by Django 3.0.5 on 2022-11-23 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0027_about"),
    ]

    operations = [
        migrations.CreateModel(
            name="WE_DO",
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
                ("we_do", models.TextField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name="about",
            name="we_do",
        ),
    ]
