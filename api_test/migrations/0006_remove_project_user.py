# Generated by Django 2.0.1 on 2018-02-08 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0005_auto_20180207_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
    ]