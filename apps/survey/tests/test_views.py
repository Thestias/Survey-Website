from django.test import TestCase
from apps.survey.models import Survey, Question
from django.contrib.auth.models import User
from django.shortcuts import reverse
import json
from django.http import HttpResponseRedirect, HttpResponse


class CommonSetUp(TestCase):
    def setUp(self):
        User.objects.create(username='UserTest123', password='test1234')
        User.objects.create(username='UserTestSecond', password='test11111')
        Survey.objects.create(
            author=User.objects.get(id=1),
            title='Title Test', description='Test Test Test')


class TestSurvey_ajax_edit_questions_view(CommonSetUp, TestCase):
    def setUp(self):
        super().setUp()
        self.data = {
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

    def test_edit_questions(self):
        '''
        This method send a POST request to the ajax_edit_questions view to test if can create a Question and a Option
        '''
        survey_test = Survey.objects.get(pk=1)
        self.client.force_login(User.objects.get(id=1))
        self.client.post(reverse('ajax_edit_questions', args=[str(survey_test.id)]), data=self.data)
        self.assertEqual(Question.objects.count(), 1)

    def test_survey_no_exist(self):
        '''
        This method tests what happens when a Survey that doesnt exist is passed to the ajax_edit_questions view
        '''
        self.client.force_login(User.objects.get(id=1))
        response = self.client.post(reverse('ajax_edit_questions', args=['11111']))
        self.assertEqual(404, response.status_code)
        self.assertEqual({'Error': 'This Survey doesnt exist!'}, json.loads(response.content))

    def test_not_the_owner(self):
        '''
        This method tests what happens when a User isnt the owner of the requested Survey
        '''
        self.client.force_login(User.objects.get(pk=2))
        survey = Survey.objects.get(pk=1)
        response = self.client.post(reverse('ajax_edit_questions', args=[str(survey.id)]))
        self.assertEqual(401, response.status_code)
        self.assertEqual({'Error': 'You are not the owner of this survey!'}, json.loads(response.content))

    def test_invalid_edit_questions_data(self):
        '''
        This method tests what happens when a user is triying to edit questions with invalid payload
        '''
        self.data['question_set-0-survey'] = ['121212']  # This invalidates the Survey

        self.client.force_login(User.objects.get(pk=1))
        survey_test = Survey.objects.get(pk=1)
        response = self.client.post(reverse('ajax_edit_questions', args=[str(survey_test.id)]), data=self.data)

        self.assertEqual(406, response.status_code)
        self.assertEqual('Error while creating survey', json.loads(response.content)['Error'])


class TestSurvey_edit_questions_view(CommonSetUp, TestCase):
    def setUp(self):
        super().setUp()

    def test_Survey_doesnt_exist(self):
        '''
        Checks that the edit_questions view returns a 404 Status code when a Survey that doesnt exist is requested
        '''
        self.client.force_login(User.objects.get(id=1))
        response = self.client.get(reverse('edit_questions', args=['1212']))

        self.assertEqual(404, response.status_code)

    def test_not_owner_redirect(self):
        '''
        Checks that the edit_questions view returns a 302(redirect) status code and a HttpResponseRedirect instance
        when a User requests a Survey from another
        '''
        self.client.force_login(User.objects.get(id=2))
        Survey.objects.get(pk=1)
        response = self.client.get(reverse('edit_questions', args=['1']))

        self.assertEqual(302, response.status_code)
        self.assertIsInstance(response, HttpResponseRedirect)

    def test_correct_view_render(self):
        '''
        Checks that the view edit_questions returns a proper 200 status code and a HttpResponse
        '''
        Survey.objects.get(pk=1)
        self.client.force_login(User.objects.get(id=1))
        response = self.client.get(reverse('edit_questions', args=['1']))

        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response, HttpResponse)


class TestSurvey_survey_view(CommonSetUp, TestCase):
    def setUp(self):
        super().setUp()
        self.client.force_login(User.objects.get(id=1))

    def test_Survey_doesnt_exist(self):
        '''
        Checks that the edit_questions view returns a 404 Status code when a Survey that doesnt exist is requested
        '''
        response = self.client.get(reverse('survey', args=['1212']))

        self.assertEqual(404, response.status_code)

    def test_Survey_delete(self):
        response = self.client.post(reverse('survey', args=['1']), data={'delete': '1'})

        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertEqual(response.url, '/profile/')

    def test_Survey_edit_valid(self):
        data = {'title': ['test'], 'description': ['testtest'], 'is_active': ['on']}

        response = self.client.post(reverse('survey', args=['1']), data=data)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "success")
        self.assertTrue("Survey updated!" in message.message)

    def test_Survey_edit_invalid(self):
        data = {'is_active': ['on']}
        response = self.client.post(reverse('survey', args=['1']), data=data)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue("Invalid form!" in message.message)

    def test_not_the_owner(self):
        response = self.client.get(reverse('survey', args=['1']))
        self.assertTrue('survey_edit_form' in response.context)
