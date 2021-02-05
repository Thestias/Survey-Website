from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Survey(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()
    is_public = models.BooleanField()

    def __str__(self):
        return f'Survey Title: {self.title} - Author_ID: {self.author} - Is active?: {self.is_active} - Is Public?: {self.is_public}'


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)

    def __str__(self):
        return f'From the Survey_ID: {self.survey} - Question: {self.question}'


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=256)


class Submission(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
