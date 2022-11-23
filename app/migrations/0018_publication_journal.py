# Generated by Django 3.0.5 on 2022-11-22 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20221122_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='journal',
            field=models.CharField(choices=[('P', 'JOURNAL_PUBLICATION'), ('C', 'CONFERENCE_PUBLICATION')], default='P', max_length=1),
        ),
    ]