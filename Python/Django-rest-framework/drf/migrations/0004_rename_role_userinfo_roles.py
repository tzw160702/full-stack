# Generated by Django 3.2.5 on 2021-09-18 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_userinfo_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='role',
            new_name='roles',
        ),
    ]
