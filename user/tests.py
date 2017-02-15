from django.test import TestCase, Client
from .models import User
from datetime import date, timedelta


class UserAppTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_list_view(self):
        user_1 = User(username='user_1', password='test')
        user_2 = User(username='user_2', password='test')
        user_1.save()
        user_2.save()

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200, '`/users/`route should load')
        self.assertEqual(len(response.context['user_list']), 2, 'It should load 2 users')
        self.assertTrue(user_1.username in str(response.content), 'It should render the user_1')

    def test_user_detail_view(self):
        user_1 = User(username='user_1', password='test')
        user_1.save()

        response = self.client.get('/users/1/')

        self.assertEqual(response.status_code, 200, '`user-detail`route should load')
        self.assertTrue(isinstance(response.context['user'], User), 'It should return a User model')
        self.assertTrue(user_1.username in str(response.content), 'It should render the user_1')

    def test_allowed(self):
        age_gt_13 = date.today() - timedelta(days=(365 * 14))
        user_1 = User(username='user_1', password='test', date_of_birth=age_gt_13)
        user_1.save()

        response = self.client.get('/users/1/')

        self.assertTrue('Allowed' in str(response.content), 'It should render `Allowed` when age > 13')

    def test_blocked(self):
        age_lt_13 = date.today() - timedelta(days=(365 * 12))
        user_1 = User(username='user_1', password='test', date_of_birth=age_lt_13)
        user_1.save()

        response = self.client.get('/users/1/')

        self.assertTrue('Blocked' in str(response.content), 'It should render `Blocked` when age < 13')

    def test_fizz(self):
        user_1 = User(username='user_1', password='test', random_number=3)
        user_1.save()

        response = self.client.get('/users/1/')

        self.assertTrue('Fizz' in str(response.content), 'It should render `Fizz` when `number % 3 == 0`')

    def test_buzz(self):
        user_1 = User(username='user_1', password='test', random_number=5)
        user_1.save()

        response = self.client.get('/users/1/')

        self.assertTrue('Buzz' in str(response.content), 'It should render `Buzz` when `number % 5 == 0`')
