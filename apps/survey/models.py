from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

# Create your models here.


class Survey(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, default='title')
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=3000, default='description')
    is_active = models.BooleanField(default=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)

    def __str__(self):
        return self.question


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=256)

    def __str__(self):
        return self.option


class Submission(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Submission for: ' + str(self.survey)


class Answer(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)

    def __str__(self):
        return 'Question: ' + str(self.question) + ' - Answer: ' + str(self.option)
