# Generated by Django 4.0.6 on 2022-08-18 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_app', '0010_alter_keyword_most_recent'),
    ]

    operations = [
        migrations.CreateModel(
            name='RandomVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=300)),
                ('video_description', models.CharField(max_length=600)),
                ('video_id', models.CharField(max_length=20)),
                ('channel_title', models.CharField(max_length=100)),
                ('upload_date', models.CharField(max_length=100)),
                ('channel_id', models.CharField(max_length=100)),
                ('video_thumbnail_pic', models.CharField(max_length=100)),
            ],
        ),
    ]