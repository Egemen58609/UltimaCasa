# Generated by Django 4.1 on 2023-10-24 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0007_remove_member_lname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bieding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateField()),
                ('bod', models.IntegerField()),
                ('statusdatum', models.DateField()),
            ],
        ),
    ]
