# Generated by Django 4.0.6 on 2022-07-17 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_user_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='author',
        ),
    ]
