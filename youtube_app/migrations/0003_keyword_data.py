# Generated by Django 4.0.6 on 2022-08-01 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_app', '0002_category_keyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
