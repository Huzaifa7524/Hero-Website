# Generated by Django 4.0.6 on 2022-08-25 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_app', '0019_remove_keyword_avatar_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AthleteProfileCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='AthleteProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar_image', models.ImageField(blank=True, null=True, upload_to='upload_images/', verbose_name='Avatar')),
                ('banner_image', models.ImageField(blank=True, null=True, upload_to='upload_images/', verbose_name='Banner Image')),
                ('age', models.IntegerField()),
                ('country', models.CharField(max_length=200)),
                ('experience', models.CharField(max_length=400)),
                ('bio', models.CharField(max_length=500)),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtube_app.keyword')),
            ],
        ),
    ]