# Generated by Django 4.1.4 on 2024-08-28 11:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0041_dataset_github"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="description",
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
