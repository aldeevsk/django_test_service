from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', index_page, name='home'),
    path('quiz/<slug:quiz_slug>', quiz_page, name='quiz'),
]
