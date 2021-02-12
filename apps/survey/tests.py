from django.test import TestCase
from apps.survey.models import Survey, Question, Option, Submission, Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import reverse
# Create your tests here.


class SurveyAppTests(TestCase):

    def setUp(self):
        User.objects.create(username='UserTest123', password='test1234')

    def test_models_dunder_str(self):
        '''
        This method tests all the dunder str methods from all the survey app models.
        '''

        survey_test = Survey.objects.create(
            author=User.objects.get(id=1),
            title='Title Test', description='Test Test Test')
        question_test = Question.objects.create(survey=Survey.objects.get(id=1), question='This is a test?')
        option_test = Option.objects.create(question=Question.objects.get(id=1), option='Option Test')
        submission_test = Submission.objects.create(survey=Survey.objects.get(id=1))
        answer_test = Answer.objects.create(
            submission=Submission.objects.get(id=1),
            question=Question.objects.get(id=1),
            option=Option.objects.get(id=1))

        self.assertEqual(str(survey_test), 'Title Test')
        self.assertEqual(str(question_test), 'This is a test?')
        self.assertEqual(str(option_test), 'Option Test')
        self.assertEqual(str(submission_test), 'Submission for: ' + str(submission_test.survey))
        self.assertEqual(
            str(answer_test),
            'Question: ' + str(answer_test.question) + ' - Answer: ' + str(answer_test.option))

    def test_view_ajax_edit_questions(self):
        data = {
            'question_set-TOTAL_FORMS': ['1'],
            'question_set-INITIAL_FORMS': ['0'],
            'question_set-MIN_NUM_FORMS': ['0'],
            'question_set-MAX_NUM_FORMS': ['1000'],
            'question_set-0-question': ['Test Question'],
            'question_set-0-id': [''],
            'question_set-0-survey': ['1'],
            'option-question_set-0-option_set-TOTAL_FORMS': ['1'],
            'option-question_set-0-option_set-INITIAL_FORMS': ['0'],
            'option-question_set-0-option_set-MIN_NUM_FORMS': ['0'],
            'option-question_set-0-option_set-MAX_NUM_FORMS': ['1000'],
            'option-question_set-0-option_set-0-option': ['Test Option'],
            'option-question_set-0-option_set-0-id': [''],
            'option-question_set-0-option_set-0-question': ['']
        }
        survey_test = Survey.objects.create(
            author=User.objects.get(id=1),
            title='Title Test', description='Test Test Test')
        self.client.force_login(User.objects.get(id=1))
        response = self.client.post(reverse('ajax_edit_questions', args=[str(survey_test.id)]), data=data)
        self.assertEqual(Question.objects.count(), 1)
