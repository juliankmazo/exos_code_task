from datetime import date, timedelta
from django.test import TestCase, Client
from .models import User


class UserAppTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_list_view(self):
        user_1 = User(username='user_1', password='test')
        user_2 = User(username='user_2', password='test')
        user_1.save()
        user_2.save()

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['user_list']), 2)
        self.assertIn(user_1.username, str(response.content))

    def test_user_detail_view(self):
        user_1 = User(username='user_1', password='test')
        user_1.save()

        response = self.client.get('/users/1/')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.context['user'], User))
        self.assertIn(user_1.username, str(response.content))

    def test_allowed(self):
        age_gt_13 = date.today() - timedelta(days=(365 * 14))
        user_1 = User(username='user_1', password='test', date_of_birth=age_gt_13)
        user_1.save()

        response = self.client.get('/users/1/')

        self.assertIn('Allowed', str(response.content))

    def test_blocked(self):
        age_lt_13 = date.today() - timedelta(days=(365 * 12))
        user_1 = User(username='user_1', password='test', date_of_birth=age_lt_13)
        user_1.save()

        response = self.client.get('/users/1/')

        self.assertIn('Blocked', str(response.content))

    def test_bizz(self):
        user_1 = User(username='user_1', password='test', random_number=3)
        user_1.save()

        response = self.client.get('/users/1/')

        self.assertIn('Bizz', str(response.content))

    def test_fuzz(self):
        user_1 = User(username='user_1', password='test', random_number=5)
        user_1.save()

        response = self.client.get('/users/1/')

        self.assertIn('Fuzz', str(response.content))

    def test_bizz_fuzz(self):
        user_1 = User(username='user_1', password='test', random_number=15)
        user_1.save()

        response = self.client.get('/users/1/')

        self.assertIn('BizzFuzz', str(response.content))
