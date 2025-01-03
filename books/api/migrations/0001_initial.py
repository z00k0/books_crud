# Generated by Django 5.1.3 on 2024-11-27 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('author', models.CharField(max_length=255, verbose_name='Автор')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('isbn', models.CharField(blank=True, max_length=255, null=True, verbose_name='ISBN')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
