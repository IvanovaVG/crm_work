import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crm.settings")

import django
django.setup()
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class UserTest(TestCase):
    def test_get_users(self):
       self.assertEqual(User.objects.count(), 0)

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='test@test.com', username='test', password='test1234',
                                        is_staff=False, is_superuser=False)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_register_user(self):
        client = Client()
        response = client.post('/register', {'first_name': 'Valentina',
                                                        'last_name': 'Ivanova',
                                                        'password': 'Medvedeva-588',
                                                        'username': 'valentinka_i',
                                                        'email': 'test@gmail.com',
                                                         "confirm_password": "Medvedeva-588",
                                                         "is_active": 'True',
                                                         "is_superuser": 'False',
                                                         "is_staff": 'False',
                                                        })

        self.assertEqual(response.status_code, 200)

        self.assertEqual(User.objects.count(), 1)

    def test_login(self):
        client = Client()
        response = client.get('/login/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_login_user(self):
        response = self.client.post('/login/', {'login': 'valentinka_i', 'password': 'Medvedeva-588'}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_incorrect_login_user(self):
        response = self.client.post('/login/', {'login': 'valentinka_i', 'password': 'Medvedeva'}, follow=True)
        self.assertEqual(response.status_code, 400)

    def test_logout(self):
        response = self.client.get('/logout/', follow=True)
        self.assertEqual(response.status_code, 200)