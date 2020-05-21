from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class Emailtesting(TestCase):
    def test_activation(self):
        # test that activation works fine
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            email='tet@test.com',
            password='ali123456789',
            date_of_birth='1998-05-05',
            username='username'
        )
        