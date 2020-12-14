from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, RegisterForm, AddQuestionForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


# Create your views here.

class Login(View):
    def get(self, request):
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'login_page.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = self.request.POST.get("user_name")
            password = self.request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
        else:
            return redirect('login')


class Register(View):
    def get(self, request):
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'login_page.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_name = self.request.POST.get('user_name')
            password = self.request.POST.get('password')
            User.objects.create_user(username=user_name, password=password)
            return redirect('login')
        else:
            return HttpResponseNotAllowed('Not Allowed')


class AddQuestion(View):
    def get(self, request):
        form = AddQuestionForm()
        context = {
            'form': form
        }
        return render(request, 'add_question.html', context)

    def post(self):
        pass
