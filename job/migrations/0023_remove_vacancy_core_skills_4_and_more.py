# Generated by Django 4.2.1 on 2023-06-19 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0022_remove_vacancy_terms_4_remove_vacancy_terms_5_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='Core_skills_4',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='Core_skills_5',
        ),
    ]
