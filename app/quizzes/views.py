from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Quiz, Question, Answer


def index_page(request):
    context = {
        'title': 'Home Page',
        'h1': 'Home Page',
    }
    return render(request, 'index.html', context=context)

def quiz_page(request, quiz_slug):
    quiz = Quiz.objects.filter( is_published=True, slug=quiz_slug)

    if quiz.exists():
        questions = Question.objects.filter(quiz=quiz[0].pk)

    if questions.exists():
        for question in questions:
            answers = Answer.objects.filter(question=question.pk)
            question.answers = answers

    context = {
        'title': 'Quiz',
        'h1': f'Тест - {quiz[0]}',
        'questions': questions,
    }
    return render(request, 'quiz.html', context=context)
