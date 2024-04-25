import os
from django.db import models
from django.urls import reverse

# Create your models here.


class Quiz(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Содержание')
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/", verbose_name='Изображение')
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(
        auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(
        default=True, verbose_name='Статус публикации')
    category = models.ForeignKey(
        'Category', on_delete=models.PROTECT,  verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Тесты'
        verbose_name_plural = 'Тесты'
        ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField(
        max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')
    image = models.ImageField(
        upload_to="photos/%Y/%m/%d/", verbose_name='Изображение')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['name']
