# Generated by Django 5.0.1 on 2024-02-11 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_rename_user_likes_image_users_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='users_likes',
            new_name='users_like',
        ),
    ]
