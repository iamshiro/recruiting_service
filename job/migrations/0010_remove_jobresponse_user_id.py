# Generated by Django 4.2.1 on 2023-05-21 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_rename_uuid_jobresponse_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobresponse',
            name='user_id',
        ),
    ]
