# Generated by Django 3.0.5 on 2022-11-15 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='cap',
            field=models.CharField(max_length=50, null=True),
        ),
    ]