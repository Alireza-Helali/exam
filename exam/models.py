from django.db import models


# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=50, unique=True)
    question = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"{self.id}/{self.title.replace(' ', '-')}"


class Answer(models.Model):
    answer = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer
