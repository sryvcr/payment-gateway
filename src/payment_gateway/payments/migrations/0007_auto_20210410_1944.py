# Generated by Django 3.1.3 on 2021-04-10 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_usercreditcard'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercreditcard',
            old_name='users',
            new_name='user',
        ),
    ]
