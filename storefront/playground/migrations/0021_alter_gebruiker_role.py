# Generated by Django 4.1 on 2023-11-15 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0020_gebruiker_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gebruiker',
            name='role',
            field=models.ForeignKey(default='koper', null=True, on_delete=django.db.models.deletion.CASCADE, to='playground.role'),
        ),
    ]
