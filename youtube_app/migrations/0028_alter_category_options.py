# Generated by Django 4.0.6 on 2022-09-03 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_app', '0027_alter_randomvideo_channel_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Lane', 'verbose_name_plural': 'Lanes'},
        ),
    ]