# Generated by Django 4.2.1 on 2023-05-21 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_alter_jobresponse_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobresponse',
            old_name='uuid',
            new_name='user_id',
        ),
    ]
