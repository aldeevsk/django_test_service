from django.contrib.admin import AdminSite
from django.contrib.admin import ModelAdmin, TabularInline, register
from .models import Category, Quiz, Question, Answer


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {
        'slug': ('title',)
    }


@register(Quiz)
class QuizAdmin(ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }


class AnswerTabularInline(TabularInline):
    model = Answer
    min_num = 2
    extra = 0
    # list_display = ('question', 'text', 'is_correct')


@register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = ('quiz', 'text')
    inlines = (AnswerTabularInline,)
    pass
