# Generated by Django 4.0.6 on 2022-07-28 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=300)),
                ('video_description', models.CharField(max_length=600)),
                ('video_id', models.CharField(max_length=20)),
                ('channel_title', models.CharField(max_length=100)),
                ('upload_date', models.CharField(max_length=100)),
                ('channel_profile_pic', models.CharField(max_length=100)),
                ('video_thumbnail_pic', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
