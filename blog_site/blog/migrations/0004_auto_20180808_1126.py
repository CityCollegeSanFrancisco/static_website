# Generated by Django 2.1 on 2018-08-08 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180808_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(help_text="Add a keyword to tag the post for easy discovery, e.g.'Python', 'Game Analysis',etc", max_length=20),
        ),
    ]