# Generated by Django 5.0.4 on 2024-04-25 16:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='слаг')),
                ('description', models.CharField(default='', max_length=255, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'db_table': 'categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='слаг')),
                ('text', models.CharField(max_length=100, verbose_name='текст вопроса')),
            ],
            options={
                'verbose_name': 'вопрос',
                'verbose_name_plural': 'вопросы',
                'db_table': 'questions',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.question', verbose_name='ответ')),
            ],
            options={
                'verbose_name': 'ответ',
                'verbose_name_plural': 'ответы',
                'db_table': 'answers',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='слаг')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='обновлен')),
                ('is_published', models.BooleanField(default=True, verbose_name='статус публикации')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quizzes.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'тест',
                'verbose_name_plural': 'тесты',
                'db_table': 'quizzes',
                'ordering': ['-time_create', 'title'],
            },
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.quiz', verbose_name='тест'),
        ),
    ]