# Generated by Django 4.0.6 on 2022-08-25 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_app', '0017_keyword_avatar_image_keyword_banner_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='avatar_image',
            field=models.ImageField(blank=True, null=True, upload_to='upload_images/', verbose_name='Avatar'),
        ),
    ]
