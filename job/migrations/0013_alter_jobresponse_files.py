# Generated by Django 4.2.1 on 2023-05-21 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_jobresponse_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobresponse',
            name='files',
            field=models.FileField(default='', upload_to='Uploaded Files/'),
        ),
    ]