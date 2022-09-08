# Generated by Django 3.2.15 on 2022-09-07 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_app', '0032_blacklistvideos'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityProfileCategory',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(default='', max_length=300)),
            ],
            options={
                'verbose_name': 'community Profile Categories',
                'verbose_name_plural': 'community Profile Categories',
            },
        ),
        migrations.AlterModelOptions(
            name='athleteprofile',
            options={'verbose_name': 'Athlete Profiles', 'verbose_name_plural': 'Athlete Profiles'},
        ),
        migrations.AlterModelOptions(
            name='athleteprofilecategory',
            options={'verbose_name': 'Athlete Profile Categories', 'verbose_name_plural': ' Athlete Profile Categories'},
        ),
        migrations.CreateModel(
            name='CommunityProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar_image', models.ImageField(blank=True, null=True, upload_to='upload_images/', verbose_name='Avatar')),
                ('banner_image', models.ImageField(blank=True, null=True, upload_to='upload_images/', verbose_name='Banner Image')),
                ('age', models.IntegerField()),
                ('country', models.CharField(max_length=200)),
                ('experience', models.CharField(max_length=400)),
                ('bio', models.CharField(max_length=500)),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtube_app.keyword')),
                ('profile_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='youtube_app.communityprofilecategory')),
            ],
            options={
                'verbose_name': 'Community Profiles',
                'verbose_name_plural': 'Community Profiles',
            },
        ),
    ]