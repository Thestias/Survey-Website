from django.test import TestCase
from apps.survey.models import Survey, Question, Option, Submission, Answer
from django.contrib.auth.models import User
from django.shortcuts import reverse
import json
from django.http import HttpResponseRedirect, HttpResponse
# Create your tests here.


class SurveyAppTests(TestCase):

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

    def test_view_ajax_edit_questions(self):
        '''
        This method send a POST request to the ajax_edit_questions view to test if can create a Question and a Option
        '''
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
        survey_test = Survey.objects.get(pk=1)
        self.client.force_login(User.objects.get(id=1))
        self.client.post(reverse('ajax_edit_questions', args=[str(survey_test.id)]), data=data)
        self.assertEqual(Question.objects.count(), 1)

    def test_view_ajax_edit_questions_survey_no_exist(self):
        '''
        This method tests what happens when a Survey that doesnt exist is passed to the ajax_edit_questions view
        '''
        self.client.force_login(User.objects.get(id=1))
        response = self.client.post(reverse('ajax_edit_questions', args=['11111']))
        self.assertEqual(404, response.status_code)
        self.assertEqual({'Error': 'This Survey doesnt exist!'}, json.loads(response.content))

    def test_view_ajax_edit_questions_survey_no_owner(self):
        '''
        This method tests what happens when a User isnt the owner of the requested Survey
        '''
        self.client.force_login(User.objects.get(pk=2))
        survey = Survey.objects.get(pk=1)
        response = self.client.post(reverse('ajax_edit_questions', args=[str(survey.id)]))
        self.assertEqual(401, response.status_code)
        self.assertEqual({'Error': 'You are not the owner of this survey!'}, json.loads(response.content))

    def test_view_ajax_edit_questions_survey_cant_create(self):
        '''
        This method tests what happens when a user is triying to edit questions with invalid payload
        '''
        data = {
            'question_set-TOTAL_FORMS': ['1'],
            'question_set-INITIAL_FORMS': ['0'],
            'question_set-MIN_NUM_FORMS': ['0'],
            'question_set-MAX_NUM_FORMS': ['1000'],
            'question_set-0-question': ['Test Question'],
            'question_set-0-id': [''],
            'question_set-0-survey': ['1212'],  # This invalidates the inline formset, a survey with 2 doesnt exist
            'option-question_set-0-option_set-TOTAL_FORMS': ['1'],
            'option-question_set-0-option_set-INITIAL_FORMS': ['0'],
            'option-question_set-0-option_set-MIN_NUM_FORMS': ['0'],
            'option-question_set-0-option_set-MAX_NUM_FORMS': ['1000'],
            'option-question_set-0-option_set-0-option': ['Test Option'],
            'option-question_set-0-option_set-0-id': [''],
            'option-question_set-0-option_set-0-question': ['']
        }
        self.client.force_login(User.objects.get(pk=1))
        survey_test = Survey.objects.get(pk=1)
        response = self.client.post(reverse('ajax_edit_questions', args=[str(survey_test.id)]), data=data)

        self.assertEqual(406, response.status_code)
        self.assertEqual('Error while creating survey', json.loads(response.content)['Error'])

    def test_view_edit_questions_Survey_doesnt_exist(self):
        '''
        Checks that the edit_questions view returns a 404 Status code when a Survey that doesnt exist is requested
        '''
        self.client.force_login(User.objects.get(id=1))
        response = self.client.get(reverse('edit_questions', args=['1212']))

        self.assertEqual(404, response.status_code)

    def test_view_edit_questions_not_owner_redirect(self):
        '''
        Checks that the edit_questions view returns a 302(redirect) status code and a HttpResponseRedirect instance
        when a User requests a Survey from another
        '''
        self.client.force_login(User.objects.get(id=2))
        Survey.objects.get(pk=1)
        response = self.client.get(reverse('edit_questions', args=['1']))

        self.assertEqual(302, response.status_code)
        self.assertIsInstance(response, HttpResponseRedirect)

    def test_view_edit_questions_correct_render(self):
        '''
        Checks that the view edit_questions returns a proper 200 status code and a HttpResponse
        '''
        Survey.objects.get(pk=1)
        self.client.force_login(User.objects.get(id=1))
        response = self.client.get(reverse('edit_questions', args=['1']))

        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response, HttpResponse)
