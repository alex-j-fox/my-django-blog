# Generated by Django 5.0.7 on 2024-08-08 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлено'),
        ),
    ]
