# Generated by Django 4.1 on 2023-10-24 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('playground', '0010_role_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.AddField(
            model_name='bieding',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='playground.home'),
        ),
        migrations.AddField(
            model_name='bieding',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='home',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
