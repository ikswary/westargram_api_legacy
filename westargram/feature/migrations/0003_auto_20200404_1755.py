# Generated by Django 3.0.5 on 2020-04-04 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feature', '0002_userdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='comment',
            new_name='password',
        ),
    ]
