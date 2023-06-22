# Generated by Django 4.2.1 on 2023-05-21 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='Core_skills_6',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='Core_skills_7',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='Requirements_10',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='Requirements_6',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='Requirements_7',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='Requirements_8',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='Requirements_9',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='Responsibilities_10',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='Responsibilities_6',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='Responsibilities_7',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='Responsibilities_8',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='Responsibilities_9',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='Terms_10',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='Terms_6',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='Terms_7',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='Terms_8',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='Terms_9',
        ),
        migrations.AddField(
            model_name='jobresponse',
            name='staus',
            field=models.CharField(choices=[('N', 'Новый отклик'), ('I', 'В процессе рассмотрения'), ('C', 'Закрытый отклик')], default='N', max_length=1),
        ),
    ]
