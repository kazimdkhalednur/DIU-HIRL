# Generated by Django 3.0.5 on 2022-11-22 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20221122_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='publication_type',
            field=models.CharField(choices=[('J', 'JOURNAL_PUBLICATION'), ('C', 'CONFERENCE_PUBLICATION')], default='J', max_length=1),
        ),
    ]