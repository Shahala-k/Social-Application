# Generated by Django 4.1.5 on 2023-02-23 08:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0005_alter_posts_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='Following',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
