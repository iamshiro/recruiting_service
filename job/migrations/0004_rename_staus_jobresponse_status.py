# Generated by Django 4.2.1 on 2023-05-21 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_jobresponse_staus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobresponse',
            old_name='staus',
            new_name='status',
        ),
    ]