from django.test import TestCase
from apps.survey.models import Survey, Question, Option, Submission, Answer
from django.contrib.auth.models import User
# Create your tests here.


class SurveyAppModelTests(TestCase):

    def setUp(self):
        User.objects.create(username='UserTest123', password='test1234')
        User.objects.create(username='UserTestSecond', password='test11111')
        Survey.objects.create(
            author=User.objects.get(id=1),
            title='Title Test', description='Test Test Test')

    def test_models_dunder_str(self):
        '''
        This method tests all the dunder str methods from all the survey app models.
        '''

        survey_test = Survey.objects.get(pk=1)
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
