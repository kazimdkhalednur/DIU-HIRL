# Generated by Django 3.0.5 on 2022-11-29 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_auto_20221128_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_type', models.CharField(default='Journal', max_length=10)),
                ('reference', models.TextField(default=True, max_length=500)),
                ('paper_link', models.URLField(blank=True, max_length=300)),
                ('category', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='app.Year')),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_type', models.CharField(default='Conference', max_length=10)),
                ('reference', models.TextField(default=True, max_length=500)),
                ('paper_link', models.URLField(blank=True, max_length=300)),
                ('category', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='app.Year')),
            ],
        ),
    ]