# Generated by Django 3.0.5 on 2022-11-28 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_auto_20221127_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_year', models.CharField(max_length=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='publication',
            name='publisher_name',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='research_title',
        ),
        migrations.AddField(
            model_name='publication',
            name='reference',
            field=models.TextField(default=True, max_length=500),
        ),
        migrations.AddField(
            model_name='publication',
            name='category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='app.Year'),
        ),
    ]
