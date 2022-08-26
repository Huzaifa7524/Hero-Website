# Generated by Django 4.0.6 on 2022-08-26 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_app', '0022_alter_randomvideo_video_thumbnail_pic_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='random_category',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='randomvideo',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='youtube_app.category'),
        ),
    ]