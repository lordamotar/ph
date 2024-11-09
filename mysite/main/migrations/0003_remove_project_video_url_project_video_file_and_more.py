# Generated by Django 5.1.2 on 2024-10-25 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_project_video_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='video_url',
        ),
        migrations.AddField(
            model_name='project',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='portfolio/videos/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio/images/'),
        ),
    ]
