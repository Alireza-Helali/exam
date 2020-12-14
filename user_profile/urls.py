from django.urls import path
from .views import Login, Register, AddQuestion

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('signup/', Register.as_view(), name='register'),
    path('', AddQuestion.as_view(), name='addquest'),
]
