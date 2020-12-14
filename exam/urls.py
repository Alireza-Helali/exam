from django.urls import path
from .views import HomePage, QuestionDetail, QuestionList

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('<pk>/<question>', QuestionDetail.as_view(), name='detail'),
    path('questions', QuestionList.as_view(), name='questions')
]
