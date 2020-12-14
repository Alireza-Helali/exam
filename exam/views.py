from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Question


# Create your views here.

class HomePage(ListView):
    queryset = Question.objects.all()[:5]
    template_name = 'home-page.html'
    context_object_name = 'questions'


class QuestionDetail(DetailView):
    template_name = 'question_detail.html'
    context_object_name = 'question'

    def get_queryset(self):
        question_id = self.kwargs.get('pk')
        question = Question.objects.filter(id=question_id)
        return question


class QuestionList(ListView):
    template_name = 'filter_quest.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('q')
        qs = Question.objects.all()
        if query:
            qs = Question.objects.filter(question__icontains=query)
        return qs
