# Generated by Django 2.0.3 on 2018-03-13 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_post_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_picture',
            new_name='post_image',
        ),
    ]