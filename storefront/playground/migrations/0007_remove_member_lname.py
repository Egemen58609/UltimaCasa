# Generated by Django 4.1 on 2023-10-11 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0006_rename_fname_member_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='lname',
        ),
    ]
