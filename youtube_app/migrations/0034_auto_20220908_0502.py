# Generated by Django 3.2.15 on 2022-09-08 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_app', '0033_auto_20220908_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='blacklistvideos',
            name='channel_id',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='blacklistvideos',
            name='video_id',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
