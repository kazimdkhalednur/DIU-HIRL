# Generated by Django 4.1.4 on 2024-08-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0039_alter_team_m_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="research",
            name="image",
            field=models.ImageField(null=True, upload_to="active_research/%y"),
        ),
    ]
