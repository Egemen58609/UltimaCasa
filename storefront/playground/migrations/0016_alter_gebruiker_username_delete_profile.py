# Generated by Django 4.1 on 2023-10-27 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0015_remove_gebruiker_passwd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gebruiker',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
