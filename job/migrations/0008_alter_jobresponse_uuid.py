# Generated by Django 4.2.1 on 2023-05-21 06:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_alter_jobresponse_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobresponse',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]