# Generated by Django 4.2.1 on 2023-05-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0017_vacancy_work_busy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Отображать вакансию'),
        ),
    ]
