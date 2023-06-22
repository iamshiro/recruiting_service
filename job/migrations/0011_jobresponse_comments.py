# Generated by Django 4.2.1 on 2023-05-21 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_remove_jobresponse_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobresponse',
            name='comments',
            field=models.CharField(choices=[('A', 'Некорректно заполнен отклик'), ('B', 'Штат сотрудников уже полон'), ('C', 'Дублирующий отклик'), ('D', 'Кандидат не подходит по критериям'), ('E', 'Кандидат подходит')], default=' ', max_length=1, verbose_name='Решение по отклику'),
        ),
    ]