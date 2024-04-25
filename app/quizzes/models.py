from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField( max_length=100, db_index=True, verbose_name='категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='слаг')
    description = models.CharField(max_length=255, blank=True, verbose_name='описание')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('categories', kwargs={'category_slug': self.slug})

    class Meta:
        db_table = 'categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['title']


class Quiz(models.Model):
    title = models.CharField(max_length=255, verbose_name='заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='слаг')
    description = models.TextField(blank=True, verbose_name='описание')
    time_create = models.DateTimeField( auto_now_add=True, verbose_name='создан')
    time_update = models.DateTimeField( auto_now=True, verbose_name='обновлен')
    is_published = models.BooleanField( default=True, verbose_name='статус публикации')
    category = models.ForeignKey( 'Category', on_delete=models.PROTECT,  verbose_name='категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('quizzes', kwargs={'quiz_slug': self.slug})

    class Meta:
        db_table = 'quizzes'
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'
        ordering = ['-time_create', 'title']


class Question(models.Model):
    text = models.CharField(max_length=255, verbose_name='текст вопроса')
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, verbose_name="тест")
    time_create = models.DateTimeField( auto_now_add=True, verbose_name='создан')
    time_update = models.DateTimeField( auto_now=True, verbose_name='обновлен')

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'questions'
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'
        ordering = ['-time_create']


class Answer(models.Model):
    text = models.CharField(max_length=100, verbose_name="ответ")
    is_correct = models.BooleanField(default=False, verbose_name="Истинность")
    question = models.ForeignKey('Question', on_delete=models.CASCADE, verbose_name="вопрос")

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'answers'
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'
