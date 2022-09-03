# Generated by Django 4.0.6 on 2022-09-03 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_app', '0026_alter_watchlist_video_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='randomvideo',
            name='channel_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Channel ID (Optional) '),
        ),
        migrations.AlterField(
            model_name='randomvideo',
            name='channel_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Channel Title (Optional) '),
        ),
        migrations.AlterField(
            model_name='randomvideo',
            name='upload_date',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Uploaded Date (Optional) '),
        ),
    ]
